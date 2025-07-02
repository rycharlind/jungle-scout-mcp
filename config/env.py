import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def get_api_key() -> str:
    """Get the Jungle Scout API key from environment variables"""
    api_key = os.getenv("JUNGLE_SCOUT_API_KEY")
    if not api_key:
        raise ValueError("JUNGLE_SCOUT_API_KEY environment variable is required")
    return api_key
