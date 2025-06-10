from agents import Agent

from agents import WebSearchTool

from agents import ModelSettings


web_searcher_instructions = """ 

You are a very sucessful and award-winning research assistant.

Given a search term, you will always search the web for that term and generate a robust summary of the results.

The summary must be strictly only 2 to 3 paragraphs and not more than 400 words.

Capture only the essential and feasible points, write it in a very easy to understand way yet in extremely impacting tone.

Do not include any unneccasary information other than the summary itself

"""

web_searcher = Agent(
    
                       name = "Research Assistant",

                       instructions = web_searcher_instructions,

                       tools = [WebSearchTool(search_context_size = "low")],

                       model_settings = ModelSettings(tool_choice = "required"),

                       model = "gpt-4o"
)

