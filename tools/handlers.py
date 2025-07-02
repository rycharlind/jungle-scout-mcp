import json
from typing import Any, Dict

from mcp.types import (
    CallToolResult,
    TextContent,
)

from models.requests import (
    ProductSearchRequest,

)
from api.jungle_scout import JungleScoutAPI


async def handle_call_tool(
    name: str, arguments: Dict[str, Any], api_client: JungleScoutAPI
) -> CallToolResult:
    """Handle tool calls"""
    try:
        if name == "search_products":
            request = ProductSearchRequest(**arguments)
            result = await api_client.search_products(
                marketplace=request.marketplace,
                page=request.page,
                page_size=request.page_size,
                product_tiers=request.product_tiers,
                seller_types=request.seller_types,
                include_keywords=request.include_keywords,
                exclude_keywords=request.exclude_keywords,
                exclude_top_brands=request.exclude_top_brands,
                exclude_unavailable_products=request.exclude_unavailable_products,
                min_price=request.min_price,
                max_price=request.max_price,
                min_net=request.min_net,
                max_net=request.max_net,
                min_rank=request.min_rank,
                max_rank=request.max_rank,
                min_sales=request.min_sales,
                max_sales=request.max_sales,
                min_revenue=request.min_revenue,
                max_revenue=request.max_revenue,
                min_reviews=request.min_reviews,
                max_reviews=request.max_reviews,
                min_rating=request.min_rating,
                max_rating=request.max_rating,
                min_weight=request.min_weight,
                max_weight=request.max_weight,
            )
            return CallToolResult(
                content=[TextContent(type="text", text=json.dumps(result, indent=2))]
            )

        else:
            raise ValueError(f"Unknown tool: {name}")

    except Exception as e:
        return CallToolResult(
            content=[
                TextContent(type="text", text=json.dumps({"error": str(e)}, indent=2))
            ],
            isError=True,
        )
