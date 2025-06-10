from pydantic import BaseModel

from agents import Agent

research_writer_instructions =  """

You are a well experienced research writer tasked to preparing a cohesive report for a research query.

You will be provided with the original query, and a few initial research draft done by a research assistant.

You must first come up with the outline of the report that talks about the structure and flow of the report.

Finally, generate the report and give that as your final output.

The final output should be in a markdown format, and it should be lengthy and detailed, yet easy to understand.

Deliver at least 5 to 7 pages of content of minimum 500 to 700 words.

"""

class ReportFormat(BaseModel):

  summary: str
  "A summary of the report generated"

  markdown_report: str
  "The final report"

  follow_up_questions: list[str]
  "Further relevant and associated research areas to discuss and explore further"


research_writer = Agent(
    
                        name = "Research Writer",

                        instructions = research_writer_instructions,

                        model = "gpt-4o",

                        output_type = ReportFormat
)