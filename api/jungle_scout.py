import httpx
from typing import Optional, Dict

JUNGLE_SCOUT_API_BASE = "https://api.junglescout.com"

class JungleScoutAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = JUNGLE_SCOUT_API_BASE
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    async def make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        async with httpx.AsyncClient() as client:
            url = f"{self.base_url}{endpoint}"
            response = await client.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()

    async def search_keywords(self, keyword: str, marketplace: str = "US", page: int = 1, page_size: int = 20) -> Dict:
        params = {
            "keyword": keyword,
            "marketplace": marketplace,
            "page": page,
            "page_size": page_size
        }
        return await self.make_request("/api/v1/keywords/search", params)

    async def search_products(self, query: str, marketplace: str = "US", page: int = 1, page_size: int = 20) -> Dict:
        params = {
            "query": query,
            "marketplace": marketplace,
            "page": page,
            "page_size": page_size
        }
        return await self.make_request("/api/v1/products/search", params)

    async def get_product_details(self, asin: str, marketplace: str = "US") -> Dict:
        params = {
            "asin": asin,
            "marketplace": marketplace
        }
        return await self.make_request("/api/v1/products/details", params)

    async def analyze_keyword(self, keyword: str, marketplace: str = "US") -> Dict:
        params = {
            "keyword": keyword,
            "marketplace": marketplace
        }
        return await self.make_request("/api/v1/keywords/analyze", params)

    async def search_categories(self, query: str, marketplace: str = "US") -> Dict:
        params = {
            "query": query,
            "marketplace": marketplace
        }
        return await self.make_request("/api/v1/categories/search", params)

    async def get_competitor_analysis(self, asin: str, marketplace: str = "US") -> Dict:
        params = {
            "asin": asin,
            "marketplace": marketplace
        }
        return await self.make_request("/api/v1/products/competitors", params) 