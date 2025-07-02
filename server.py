#!/usr/bin/env python3
"""
Jungle Scout MCP Server for MCP Installer

This file exports a global FastMCP instance that can be used by the MCP installer
while keeping the server modules separated.
"""

from mcp.server import FastMCP
from config.env import get_api_key
from api.jungle_scout import JungleScoutAPI
from tools.handlers import handle_call_tool
from typing import List, Optional

# Initialize API client
api_client = JungleScoutAPI(get_api_key())

# Create global FastMCP instance for MCP installer
mcp = FastMCP("jungle-scout-mcp")

# Register tools with the global FastMCP instance


@mcp.tool()
async def search_products(
    marketplace: str = "US",
    page: int = 1,
    page_size: int = 50,
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
):
    """Search for products on Amazon with advanced filtering options including product tiers, seller types, keyword inclusion/exclusion, price ranges, sales metrics, review metrics, and weight ranges"""
    return await handle_call_tool(
        "search_products",
        {
            "marketplace": marketplace,
            "page": page,
            "page_size": page_size,
            "product_tiers": product_tiers,
            "seller_types": seller_types,
            "include_keywords": include_keywords,
            "exclude_keywords": exclude_keywords,
            "exclude_top_brands": exclude_top_brands,
            "exclude_unavailable_products": exclude_unavailable_products,
            "min_price": min_price,
            "max_price": max_price,
            "min_net": min_net,
            "max_net": max_net,
            "min_rank": min_rank,
            "max_rank": max_rank,
            "min_sales": min_sales,
            "max_sales": max_sales,
            "min_revenue": min_revenue,
            "max_revenue": max_revenue,
            "min_reviews": min_reviews,
            "max_reviews": max_reviews,
            "min_rating": min_rating,
            "max_rating": max_rating,
            "min_weight": min_weight,
            "max_weight": max_weight,
        },
        api_client,
    )


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
