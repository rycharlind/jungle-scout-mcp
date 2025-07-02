import httpx
from typing import Optional, Dict, List
import json
from config.constants import PRODUCT_SEARCH_LIMIT

JUNGLE_SCOUT_API_BASE = "https://developer.junglescout.com"


class JungleScoutAPI:
    def __init__(self, api_key: str, key_id: str = "inndevers1"):
        self.api_key = api_key
        self.key_id = key_id
        self.base_url = JUNGLE_SCOUT_API_BASE
        self.headers = {
            "Authorization": f"{key_id}:{api_key}",
            "Content-Type": "application/vnd.api+json",
            "Accept": "application/vnd.junglescout.v1+json",
        }

    async def make_request(
        self,
        endpoint: str,
        params: Optional[Dict] = None,
        data: Optional[Dict] = None,
        method: str = "POST",
    ) -> Dict:
        async with httpx.AsyncClient() as client:
            url = f"{self.base_url}{endpoint}"

            # Debug logging
            print(f"DEBUG: Making {method} request to {url}")
            print(f"DEBUG: Headers: {self.headers}")
            print(f"DEBUG: Params: {params}")
            print(f"DEBUG: Data: {json.dumps(data, indent=2) if data else None}")

            if method.upper() == "POST":
                response = await client.post(
                    url, headers=self.headers, params=params, json=data
                )
            else:
                response = await client.get(url, headers=self.headers, params=params)

            # Debug response
            print(f"DEBUG: Response status: {response.status_code}")
            print(f"DEBUG: Response headers: {dict(response.headers)}")
            
            if response.status_code >= 400:
                print(f"DEBUG: Error response body: {response.text}")
            
            response.raise_for_status()
            return response.json()

    def _parse_list_param(self, value):
        """Parse a list parameter that might come as a string or list"""
        if value is None:
            return None
        if isinstance(value, list):
            return value
        if isinstance(value, str):
            try:
                # Try to parse as JSON if it's a string representation of a list
                parsed = json.loads(value)
                if isinstance(parsed, list):
                    return parsed
            except (json.JSONDecodeError, TypeError):
                pass
            # If it's a single string, treat as a single-item list
            return [value]
        return None

    def _parse_numeric_param(self, value):
        """Parse a numeric parameter that might come as a string"""
        if value is None:
            return None
        if isinstance(value, (int, float)):
            return value
        if isinstance(value, str):
            try:
                # Try to parse as float first, then int
                float_val = float(value)
                # If it's a whole number, return as int
                if float_val.is_integer():
                    return int(float_val)
                return float_val
            except (ValueError, TypeError):
                return None
        return None

    def _parse_bool_param(self, value):
        """Parse a boolean parameter that might come as a string"""
        if value is None:
            return None
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.lower() in ('true', '1', 'yes', 'on')
        return bool(value)

    def _normalize_seller_types(self, seller_types):
        """Normalize seller types to lowercase to match API expectations"""
        if seller_types is None:
            return None
        
        normalized = []
        for seller_type in seller_types:
            if isinstance(seller_type, str):
                normalized.append(seller_type.lower())
            else:
                normalized.append(seller_type)
        
        return normalized

    async def search_products(
        self,
        marketplace: str = "us",
        page: int = 1,
        page_size: int = PRODUCT_SEARCH_LIMIT,
        product_tiers: Optional[List[str]] = None,
        seller_types: Optional[List[str]] = None,
        include_keywords: Optional[List[str]] = None,
        exclude_keywords: Optional[List[str]] = None,
        exclude_top_brands: Optional[bool] = None,
        exclude_unavailable_products: Optional[bool] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        min_net: Optional[float] = None,
        max_net: Optional[float] = None,
        min_rank: Optional[int] = None,
        max_rank: Optional[int] = None,
        min_sales: Optional[int] = None,
        max_sales: Optional[int] = None,
        min_revenue: Optional[float] = None,
        max_revenue: Optional[float] = None,
        min_reviews: Optional[int] = None,
        max_reviews: Optional[int] = None,
        min_rating: Optional[float] = None,
        max_rating: Optional[float] = None,
        min_weight: Optional[float] = None,
        max_weight: Optional[float] = None,
    ) -> Dict:
        # Normalize marketplace to lowercase
        marketplace = marketplace.lower() if marketplace else "us"
        
        # Parse and validate parameters
        page = self._parse_numeric_param(page) or 1
        page_size = self._parse_numeric_param(page_size) or PRODUCT_SEARCH_LIMIT
        
        # Parse list parameters
        product_tiers = self._parse_list_param(product_tiers)
        seller_types = self._parse_list_param(seller_types)
        include_keywords = self._parse_list_param(include_keywords)
        exclude_keywords = self._parse_list_param(exclude_keywords)
        
        # Parse boolean parameters
        exclude_top_brands = self._parse_bool_param(exclude_top_brands)
        exclude_unavailable_products = self._parse_bool_param(exclude_unavailable_products)
        
        # Parse numeric parameters
        min_price = self._parse_numeric_param(min_price)
        max_price = self._parse_numeric_param(max_price)
        min_net = self._parse_numeric_param(min_net)
        max_net = self._parse_numeric_param(max_net)
        min_rank = self._parse_numeric_param(min_rank)
        max_rank = self._parse_numeric_param(max_rank)
        min_sales = self._parse_numeric_param(min_sales)
        max_sales = self._parse_numeric_param(max_sales)
        min_revenue = self._parse_numeric_param(min_revenue)
        max_revenue = self._parse_numeric_param(max_revenue)
        min_reviews = self._parse_numeric_param(min_reviews)
        max_reviews = self._parse_numeric_param(max_reviews)
        min_rating = self._parse_numeric_param(min_rating)
        max_rating = self._parse_numeric_param(max_rating)
        min_weight = self._parse_numeric_param(min_weight)
        max_weight = self._parse_numeric_param(max_weight)

        # Build attributes dictionary with only non-None values
        attributes = {}
        
        if product_tiers is not None:
            attributes["product_tiers"] = product_tiers
        if seller_types is not None:
            attributes["seller_types"] = self._normalize_seller_types(seller_types)
        if include_keywords is not None:
            attributes["include_keywords"] = include_keywords
        if exclude_keywords is not None:
            attributes["exclude_keywords"] = exclude_keywords
        if exclude_top_brands is not None:
            attributes["exclude_top_brands"] = exclude_top_brands
        if exclude_unavailable_products is not None:
            attributes["exclude_unavailable_products"] = exclude_unavailable_products
        if min_price is not None:
            attributes["min_price"] = min_price
        if max_price is not None:
            attributes["max_price"] = max_price
        if min_net is not None:
            attributes["min_net"] = min_net
        if max_net is not None:
            attributes["max_net"] = max_net
        if min_rank is not None:
            attributes["min_rank"] = min_rank
        if max_rank is not None:
            attributes["max_rank"] = max_rank
        if min_sales is not None:
            attributes["min_sales"] = min_sales
        if max_sales is not None:
            attributes["max_sales"] = max_sales
        if min_revenue is not None:
            attributes["min_revenue"] = min_revenue
        if max_revenue is not None:
            attributes["max_revenue"] = max_revenue
        if min_reviews is not None:
            attributes["min_reviews"] = min_reviews
        if max_reviews is not None:
            attributes["max_reviews"] = max_reviews
        if min_rating is not None:
            attributes["min_rating"] = min_rating
        if max_rating is not None:
            attributes["max_rating"] = max_rating
        if min_weight is not None:
            attributes["min_weight"] = min_weight
        if max_weight is not None:
            attributes["max_weight"] = max_weight

        post_data = {
            "data": {
                "type": "product_database_query",
                "attributes": attributes
            }
        }
        
        # Set up query parameters
        params = {
            "marketplace": marketplace,
            "sort": "name",
            "page[size]": page_size
        }
        
        # Add page parameter if it's not the first page
        if page > 1:
            params["page[number]"] = page
        
        return await self.make_request(
            endpoint="/api/product_database_query", 
            params=params,
            data=post_data
        )
