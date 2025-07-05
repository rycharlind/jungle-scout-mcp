#!/usr/bin/env python3
"""
Test script to verify MCP server setup
"""

import asyncio
import json
from server import mcp, search_products_tool

async def test_mcp_server():
    """Test that the MCP server is properly configured"""
    
    print("Testing MCP server configuration...")
    
    # Test that the tool function exists and is callable
    print(f"✅ Tool function exists: {search_products_tool}")
    print(f"✅ Tool function is callable: {callable(search_products_tool)}")
    
    # Test a simple tool call with minimal parameters
    try:
        print("\nTesting tool call with minimal parameters...")
        result = await search_products_tool(marketplace="us", page=1)
        print("✅ Tool call successful!")
        print(f"Result type: {type(result)}")
        print(f"Result content length: {len(result.content)}")
        
        # Print first 500 characters of the result
        if result.content:
            content_text = result.content[0].text
            print(f"First 500 chars of result: {content_text[:500]}...")
        
    except Exception as e:
        print(f"❌ Tool call failed: {e}")
        import traceback
        traceback.print_exc()
    
    print("\nMCP server test completed.")

if __name__ == "__main__":
    asyncio.run(test_mcp_server()) 