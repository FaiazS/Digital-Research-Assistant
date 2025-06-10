import asyncio

from typing import Dict

from agents import trace, gen_trace_id, Runner

from web_searcher import web_searcher

from research_planner import research_planner, WebSearchItem, WebSearchResultsList

from research_writer import research_writer, ReportFormat

from email_agent import email_agent

class ResearchManager:

    async def run(self, query: str):

        """Runs the deep research process, yielding the status updates and final report."""

        trace_id = gen_trace_id()

        with trace("Research in progress", trace_id=trace_id):

            print(f"View trace: https://platform.openai.com/traces/{trace_id}")

            yield f"View trace: https://platform.openai.com/traces/{trace_id}"

            print("Initializing research.....")

            research_plan = await self.plan_search(query)

            yield "Search planning completed, preparing for search"

            search_results = await self.perform_search(research_plan)

            yield "Searches complete, drafting report...."

            research_report = await self.draft_research_report(query, search_results)

            yield "Research report drafted. Sending email with the report attached."

            await self.send_email(research_report)

            yield "Email sent successfully! Research Task completed."

            yield research_report.markdown_report


    async def plan_search(self, query: str) -> WebSearchResultsList:

        """Plans search to be perfomed for the query"""   

        print("Planning searches")

        results = await Runner.run(research_planner, f"Query:{query}")

        print(f"Will perform {len(results.final_output.web_search_results)} searches")

        return results.final_output_as(WebSearchResultsList)
    

    async def perform_search(self, research_plan: WebSearchResultsList)-> list[str]:

        """Runs the searches to perform for the query"""

        print("Searching....")

        num_completed = 0

        tasks = [asyncio.create_task(self.search(item)) for item in research_plan.web_search_results]

        results = []

        for task in asyncio.as_completed(tasks):

            result = await task

            if result is not None:

              results.append(result)

            num_completed += 1

            print(f"Searches completed: {num_completed}/{len(tasks)} completed.")

        print("Search Complete!")

        return results
        
    
    async def search(self, item: WebSearchItem) -> str | None:

        """Performs a search for the query"""

        input = f"Query : {item.query}, Reason for searching/querying: {item.query}"

        try:

            result = await Runner.run(web_searcher, input)
             
        except Exception:

            return None

    async def draft_research_report(self, query:str, search_results: list[str]) -> ReportFormat:

        """Drafting a research report for the query"""

        print("Preparing research report....")

        input = f"Original query: {query}, Summarized searches: {search_results}"

        result = await Runner.run(research_writer, input)

        print("Draft of research report completed!")

        return result.final_output_as(ReportFormat)
    

    async def send_email(self, research_report: ReportFormat) -> None:

        print("Sending email with research report attached....")

        result = await Runner.run(email_agent, research_report.markdown_report)

        print("Email sent sucessfully with research report attached!")

        return research_report
 


    










