import json
from typing import Any, Dict

from mcp.types import (
    CallToolResult,
    ListToolsResult,
    Tool,
    TextContent,
)

from models.requests import (
    KeywordSearchRequest,
    ProductSearchRequest,
    ProductDetailsRequest,
    KeywordAnalyzerRequest,
    CategorySearchRequest,
    CompetitorAnalysisRequest,
)
from api.jungle_scout import JungleScoutAPI

def get_tools() -> ListToolsResult:
    """Get all available tools"""
    return ListToolsResult(
        tools=[
            Tool(
                name="search_keywords",
                description="Search for keywords and get search volume, competition, and other metrics",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "keyword": {"type": "string", "description": "The keyword to search for"},
                        "marketplace": {"type": "string", "description": "Marketplace (US, CA, UK, DE, FR, IT, ES, JP, IN, MX, AU, BR)", "default": "US"},
                        "page": {"type": "integer", "description": "Page number for pagination", "default": 1},
                        "page_size": {"type": "integer", "description": "Number of results per page", "default": 20}
                    },
                    "required": ["keyword"]
                }
            ),
            Tool(
                name="search_products",
                description="Search for products on Amazon and get product data",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Product search query"},
                        "marketplace": {"type": "string", "description": "Marketplace (US, CA, UK, DE, FR, IT, ES, JP, IN, MX, AU, BR)", "default": "US"},
                        "page": {"type": "integer", "description": "Page number for pagination", "default": 1},
                        "page_size": {"type": "integer", "description": "Number of results per page", "default": 20}
                    },
                    "required": ["query"]
                }
            ),
            Tool(
                name="get_product_details",
                description="Get detailed product information by ASIN",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "asin": {"type": "string", "description": "Amazon ASIN of the product"},
                        "marketplace": {"type": "string", "description": "Marketplace (US, CA, UK, DE, FR, IT, ES, JP, IN, MX, AU, BR)", "default": "US"}
                    },
                    "required": ["asin"]
                }
            ),
            Tool(
                name="analyze_keyword",
                description="Analyze keyword metrics including search volume, competition, and difficulty",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "keyword": {"type": "string", "description": "The keyword to analyze"},
                        "marketplace": {"type": "string", "description": "Marketplace (US, CA, UK, DE, FR, IT, ES, JP, IN, MX, AU, BR)", "default": "US"}
                    },
                    "required": ["keyword"]
                }
            ),
            Tool(
                name="search_categories",
                description="Search for product categories on Amazon",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Category search query"},
                        "marketplace": {"type": "string", "description": "Marketplace (US, CA, UK, DE, FR, IT, ES, JP, IN, MX, AU, BR)", "default": "US"}
                    },
                    "required": ["query"]
                }
            ),
            Tool(
                name="get_competitor_analysis",
                description="Get competitor analysis for a specific product",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "asin": {"type": "string", "description": "Amazon ASIN of the product"},
                        "marketplace": {"type": "string", "description": "Marketplace (US, CA, UK, DE, FR, IT, ES, JP, IN, MX, AU, BR)", "default": "US"}
                    },
                    "required": ["asin"]
                }
            )
        ]
    )

async def handle_call_tool(name: str, arguments: Dict[str, Any], api_client: JungleScoutAPI) -> CallToolResult:
    """Handle tool calls"""
    try:
        if name == "search_keywords":
            request = KeywordSearchRequest(**arguments)
            result = await api_client.search_keywords(
                keyword=request.keyword,
                marketplace=request.marketplace,
                page=request.page,
                page_size=request.page_size
            )
            return CallToolResult(content=[TextContent(type="text", text=json.dumps(result, indent=2))])

        elif name == "search_products":
            request = ProductSearchRequest(**arguments)
            result = await api_client.search_products(
                query=request.query,
                marketplace=request.marketplace,
                page=request.page,
                page_size=request.page_size
            )
            return CallToolResult(content=[TextContent(type="text", text=json.dumps(result, indent=2))])

        elif name == "get_product_details":
            request = ProductDetailsRequest(**arguments)
            result = await api_client.get_product_details(
                asin=request.asin,
                marketplace=request.marketplace
            )
            return CallToolResult(content=[TextContent(type="text", text=json.dumps(result, indent=2))])

        elif name == "analyze_keyword":
            request = KeywordAnalyzerRequest(**arguments)
            result = await api_client.analyze_keyword(
                keyword=request.keyword,
                marketplace=request.marketplace
            )
            return CallToolResult(content=[TextContent(type="text", text=json.dumps(result, indent=2))])

        elif name == "search_categories":
            request = CategorySearchRequest(**arguments)
            result = await api_client.search_categories(
                query=request.query,
                marketplace=request.marketplace
            )
            return CallToolResult(content=[TextContent(type="text", text=json.dumps(result, indent=2))])

        elif name == "get_competitor_analysis":
            request = CompetitorAnalysisRequest(**arguments)
            result = await api_client.get_competitor_analysis(
                asin=request.asin,
                marketplace=request.marketplace
            )
            return CallToolResult(content=[TextContent(type="text", text=json.dumps(result, indent=2))])

        else:
            raise ValueError(f"Unknown tool: {name}")

    except Exception as e:
        return CallToolResult(
            content=[TextContent(type="text", text=json.dumps({"error": str(e)}, indent=2))],
            isError=True
        ) 