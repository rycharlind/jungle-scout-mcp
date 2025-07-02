from api.jungle_scout import JungleScoutAPI
import asyncio
from config.env import get_api_key


async def validate_js_api():
    api_key = get_api_key()
    print(api_key)
    api_client = JungleScoutAPI(api_key)
    try:
        print("Validating Jungle Scout API...")
        results = await api_client.search_products()
        print("API call completed successfully!")
        print("Results:", results)
        return results
    except Exception as e:
        print(f"Error occurred: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    asyncio.run(validate_js_api())
