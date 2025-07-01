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

# Initialize API client
api_client = JungleScoutAPI(get_api_key())

# Create global FastMCP instance for MCP installer
mcp = FastMCP("jungle-scout-mcp")

# Register tools with the global FastMCP instance


@mcp.tool()
async def search_keywords(keyword: str, marketplace: str = "US", page: int = 1, page_size: int = 20):
    """Search for keywords and get search volume, competition, and other metrics"""
    return await handle_call_tool("search_keywords", {
        "keyword": keyword,
        "marketplace": marketplace,
        "page": page,
        "page_size": page_size
    }, api_client)


@mcp.tool()
async def search_products(query: str, marketplace: str = "US", page: int = 1, page_size: int = 20):
    """Search for products on Amazon and get product data"""
    return await handle_call_tool("search_products", {
        "query": query,
        "marketplace": marketplace,
        "page": page,
        "page_size": page_size
    }, api_client)


@mcp.tool()
async def get_product_details(asin: str, marketplace: str = "US"):
    """Get detailed product information by ASIN"""
    return await handle_call_tool("get_product_details", {
        "asin": asin,
        "marketplace": marketplace
    }, api_client)


@mcp.tool()
async def analyze_keyword(keyword: str, marketplace: str = "US"):
    """Analyze keyword metrics including search volume, competition, and difficulty"""
    return await handle_call_tool("analyze_keyword", {
        "keyword": keyword,
        "marketplace": marketplace
    }, api_client)


@mcp.tool()
async def search_categories(query: str, marketplace: str = "US"):
    """Search for product categories on Amazon"""
    return await handle_call_tool("search_categories", {
        "query": query,
        "marketplace": marketplace
    }, api_client)


@mcp.tool()
async def get_competitor_analysis(asin: str, marketplace: str = "US"):
    """Get competitor analysis for a specific product"""
    return await handle_call_tool("get_competitor_analysis", {
        "asin": asin,
        "marketplace": marketplace
    }, api_client)


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
