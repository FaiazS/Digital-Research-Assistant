from pydantic import BaseModel

from agents import Agent

how_many_searches = 3

research_planner_agent_instructions = f"You are a fellow and a very helpful research assistant. Given a query, come up with a set of web searches to best answer the query.Output {how_many_searches} terms to query for"

class WebSearchItem(BaseModel):

  reason: str
  "Your reasoning and thought process of why this search is important to the query."

  query: str
  "The search term for to use for web searches"

class WebSearchResultsList(BaseModel):

  web_search_results : list[WebSearchItem]

  """List of relevant web links of the query search result."""

research_planner = Agent(

                               name = "Research Planner",

                               instructions = research_planner_agent_instructions,

                               output_type = WebSearchResultsList,

                               model = "gpt-4o"
)
