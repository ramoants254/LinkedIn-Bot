import datetime
import requests
import crewai
import os
from dotenv import load_dotenv
from duckduckgo_search import ddg

# Load environment variables from .env file
load_dotenv()

class ContentScoutAgent:
    def __init__(self, search_engine='serpapi'):
        self.search_engine = search_engine
        self.role = 'Content Scout'
        self.goal = "Find the top 5 articles on AI and cybersecurity every morning."
        self.backstory = "A diligent reporter who searches for the most relevant and important news on a daily basis."

    def fetch_content(self, topic='AI CyberSecurity'):
        """ Fetch top 5 articles from Serpapi """
        if self.search_engine == 'serpapi':
            url = f"https://serpapi.com/search.json?q={topic}&api_key={os.getenv('SERP_API_KEY')}"
            try:
                response = requests.get(url)
                response.raise_for_status()  # Check for HTTP errors
                articles = response.json().get('organic_results', [])
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                articles = []
        else:
            articles = ddg(topic, max_results=5)
        
        return articles[:5]
