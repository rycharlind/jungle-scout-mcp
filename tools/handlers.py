from typing import Dict, Any
from mcp.types import CallToolResult, TextContent
import json
import traceback

from api.jungle_scout import JungleScoutAPI


def create_tool_handler(request_model_class, api_method_name: str, api_client: JungleScoutAPI, additional_params: Dict[str, Any] = None):
    """Generic factory function to create tool handlers with Pydantic models"""

    async def tool_handler(**kwargs):
        """Generic tool handler that uses Pydantic models for validation and API calls"""
        try:
            # Create request model from kwargs - Pydantic will handle validation
            request = request_model_class(**kwargs)

            # Get all request parameters
            params = request.model_dump()

            # Add any additional parameters (like page_size)
            if additional_params:
                params.update(additional_params)

            # Call the appropriate API method
            api_method = getattr(api_client, api_method_name)
            result = await api_method(**params)

            return CallToolResult(
                content=[TextContent(type="text", text=json.dumps(result, indent=2))]
            )
        except Exception as e:
            # Return error in a format that MCP can handle
            error_message = f"Error: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
            return CallToolResult(
                content=[TextContent(type="text", text=error_message)]
            )

    return tool_handler
