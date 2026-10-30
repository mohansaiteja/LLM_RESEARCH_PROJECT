from datetime import datetime

from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool


@tool
def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    """Append research text to a local file, with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = (
        f"--- Research Output ---\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n\n"
    )

    with open(filename, "a", encoding="utf-8") as file:
        file.write(formatted_text)

    return f"Research data saved to {filename}"


search_tool = DuckDuckGoSearchRun()
search_tool.name = "search"
search_tool.description = "Search the web for information about the user's research query."

wiki_tool = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(
        top_k_results=1,
        doc_content_chars_max=1000,
    )
)

save_tool = save_to_txt