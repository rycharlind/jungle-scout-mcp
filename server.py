#!/usr/bin/env python3
"""
Jungle Scout MCP Server for MCP Installer

This file exports a global FastMCP instance that can be used by the MCP installer
while keeping the server modules separated.
"""

from mcp.server import FastMCP
from config.env import get_api_key, get_api_key_id
from api.jungle_scout import JungleScoutAPI
from tools.product_search import create_search_products_tool

# Initialize API client
api_client = JungleScoutAPI(get_api_key(), get_api_key_id())

# Create global FastMCP instance for MCP installer
mcp = FastMCP("jungle-scout-mcp")

# Create and register the search_products tool
search_products_tool = create_search_products_tool(api_client)
mcp.tool()(search_products_tool)


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
