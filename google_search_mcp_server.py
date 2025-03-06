"""
Google Search MCP Server

A FastMCP server that provides Google Custom Search functionality.
This server exposes a tool for performing Google searches and returning formatted results.
It requires Google API Key and Custom Search Engine ID stored in environment variables.
"""

import os
from typing import Dict, Any
from mcp.server.fastmcp import FastMCP
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

# Load configuration from .env
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_CSE_ID = os.getenv('GOOGLE_CSE_ID')

mcp = FastMCP("GoogleSearch")


@mcp.tool()
async def search_google(query: str, num_results: int = 5) -> Dict[str, Any]:
    """
    Perform a Google search and return formatted results.
    
    This function uses Google Custom Search API to search the web based on the provided query.
    It formats the results into a consistent structure and handles potential errors.
    
    Args:
        query (str): The search query string
        num_results (int, optional): Number of search results to return. Defaults to 5.
        
    Returns:
        Dict[str, Any]: A dictionary containing:
            - success (bool): Whether the search was successful
            - results (list): List of dictionaries with title, link, and snippet
            - total_results (str): Total number of results found (when successful)
            - error (str): Error message (when unsuccessful)
    """
    try:
        # Initialize Google Custom Search API
        service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
        
        # Execute the search
        # pylint: disable=no-member
        result = service.cse().list(
            q=query,
            cx=GOOGLE_CSE_ID,
            num=num_results
        ).execute()
        
        # Format the search results
        formatted_results = []
        if "items" in result:
            for item in result["items"]:
                formatted_results.append({
                    "title": item.get("title", ""),
                    "link": item.get("link", ""),
                    "snippet": item.get("snippet", "")
                })
        
        return {
            "success": True,
            "results": formatted_results,
            "total_results": result.get("searchInformation", {}).get("totalResults", "0")
        }
    
    except HttpError as error:
        return {
            "success": False,
            "error": f"API Error: {str(error)}",
            "results": []
        }
    except Exception as error:  # pylint: disable=broad-exception-caught
        return {
            "success": False,
            "error": str(error),
            "results": []
        }

if __name__ == "__main__":
    mcp.run()