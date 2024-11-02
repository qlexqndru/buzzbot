import datetime
import os
from serpapi import GoogleSearch

def summarize_search_results(results):
    summary = "Here's the latest update:\n"
    for i, result in enumerate(results[:35]):
        summary += f"{i+1}. {result['title']}: {result.get('snippet', '')} ({result.get('link', '')})\n"
    return summary if summary else "No relevant updates at this time."

class WebSearch:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("SERPAPI_API_KEY")
        if not self.api_key:
            raise ValueError("SerpAPI key is required")
        self.client = GoogleSearch({"api_key": self.api_key})

    def search(self, query, site=None, filetype=None, intitle=None, exclude=None):
        # Base query
        dork_query = query

        # Apply 'site:' operator if specified
        if site:
            dork_query += f" site:{site}"

        # Apply 'filetype:' operator if specified
        if filetype:
            dork_query += f" filetype:{filetype}"

        # Apply 'intitle:' operator if specified
        if intitle:
            dork_query += f" intitle:{intitle}"

        # Apply exclusion if specified
        if exclude:
            dork_query += f" -{exclude}"

        # Add date filter
        dork_query += f" after:{datetime.date.today().isoformat()}"

        params = {
            "engine": "google",
            "q": dork_query,
            "sort": "date",
            "num": 20,
            "api_key": self.api_key,
            "no_cache": True
        }

        # Get search results
        search_result = GoogleSearch(params).get_json()

        # Extract relevant fields from the organic results
        results = []
        for item in search_result.get("organic_results", []):
            result = {
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet")
            }
            results.append(result)

        # Return the summarized search results
        return summarize_search_results(results)

# Example usage
if __name__ == "__main__":
    web_search = WebSearch(api_key='YOUR_SERPAPI_KEY')
    summary = web_search.search(
        query='"artificial intelligence" AND "2024 trends"',
        site="edu",
        filetype="pdf",
        intitle="research",
        exclude="draft"
    )
