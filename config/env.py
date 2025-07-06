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


def get_api_key_id() -> str:
    """Get the Jungle Scout API key ID from environment variables"""
    api_key_id = os.getenv("JUNGLE_SCOUT_API_KEY_ID")
    if not api_key_id:
        raise ValueError("JUNGLE_SCOUT_API_KEY_ID environment variable is required")
    return api_key_id
