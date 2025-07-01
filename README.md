# Jungle Scout MCP Server

A Model Context Protocol (MCP) server that provides tools to interact with the Jungle Scout API for Amazon product research and keyword analysis.

## Features

This MCP server provides the following tools:

- **Keyword Search**: Search for keywords and get search volume, competition, and other metrics
- **Product Search**: Search for products on Amazon and get product data
- **Product Details**: Get detailed product information by ASIN
- **Keyword Analysis**: Analyze keyword metrics including search volume, competition, and difficulty
- **Category Search**: Search for product categories on Amazon
- **Competitor Analysis**: Get competitor analysis for a specific product

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Jungle Scout API Key

1. Go to [Jungle Scout API](https://app.junglescout.com/api/)
2. Generate your API key
3. Copy the API key

### 3. Configure Environment

Create a `.env` file in the project root:

```bash
cp env.example .env
```

Edit the `.env` file and add your API key:

```
JUNGLE_SCOUT_API_KEY=your_actual_api_key_here
```

### 4. Install for Claude Desktop (Optional)

To use this MCP server with Claude Desktop, install it using the MCP installer:

```bash
mcp install server.py
```

This will make the Jungle Scout tools available in Claude Desktop for Amazon product research and keyword analysis.

### 5. Run the MCP Server

**Production Mode (stdio):**
```bash
python main.py
```

**Development Mode (with MCP Inspector):**
```bash
python dev_server.py
```

The development mode enables HTTP server support for the MCP Inspector tool, which allows you to:
- Test your tools interactively
- Debug tool calls and responses
- View server capabilities and tool schemas
- Monitor server performance

Access the MCP Inspector at: http://localhost:8000

### Using MCP Inspector

The MCP Inspector is a web-based tool for testing and debugging MCP servers:

1. **Start the development server:**
   ```bash
   python dev_server.py
   ```

2. **Open your browser and navigate to:** http://localhost:8000

3. **Test your tools:**
   - View all available tools and their schemas
   - Make test calls to your tools
   - See real-time responses and errors
   - Debug parameter validation

4. **Monitor server performance:**
   - View request/response times
   - Check for errors and warnings
   - Monitor API rate limits

## Usage

### Tool Descriptions

#### 1. search_keywords
Search for keywords and get search volume, competition, and other metrics.

**Parameters:**
- `keyword` (required): The keyword to search for
- `marketplace` (optional): Marketplace code (US, CA, UK, DE, FR, IT, ES, JP, IN, MX, AU, BR). Default: US
- `page` (optional): Page number for pagination. Default: 1
- `page_size` (optional): Number of results per page. Default: 20

#### 2. search_products
Search for products on Amazon and get product data.

**Parameters:**
- `query` (required): Product search query
- `marketplace` (optional): Marketplace code. Default: US
- `page` (optional): Page number for pagination. Default: 1
- `page_size` (optional): Number of results per page. Default: 20

#### 3. get_product_details
Get detailed product information by ASIN.

**Parameters:**
- `asin` (required): Amazon ASIN of the product
- `marketplace` (optional): Marketplace code. Default: US

#### 4. analyze_keyword
Analyze keyword metrics including search volume, competition, and difficulty.

**Parameters:**
- `keyword` (required): The keyword to analyze
- `marketplace` (optional): Marketplace code. Default: US

#### 5. search_categories
Search for product categories on Amazon.

**Parameters:**
- `query` (required): Category search query
- `marketplace` (optional): Marketplace code. Default: US

#### 6. get_competitor_analysis
Get competitor analysis for a specific product.

**Parameters:**
- `asin` (required): Amazon ASIN of the product
- `marketplace` (optional): Marketplace code. Default: US

### Example Usage

Here are some example tool calls you can make:

```json
{
  "name": "search_keywords",
  "arguments": {
    "keyword": "wireless headphones",
    "marketplace": "US"
  }
}
```

```json
{
  "name": "search_products",
  "arguments": {
    "query": "bluetooth speaker",
    "marketplace": "US",
    "page_size": 10
  }
}
```

```json
{
  "name": "get_product_details",
  "arguments": {
    "asin": "B08N5WRWNW",
    "marketplace": "US"
  }
}
```

```json
{
  "name": "analyze_keyword",
  "arguments": {
    "keyword": "fitness tracker",
    "marketplace": "US"
  }
}
```

## Supported Marketplaces

The following marketplace codes are supported:
- US (United States)
- CA (Canada)
- UK (United Kingdom)
- DE (Germany)
- FR (France)
- IT (Italy)
- ES (Spain)
- JP (Japan)
- IN (India)
- MX (Mexico)
- AU (Australia)
- BR (Brazil)

## API Endpoints

This MCP server integrates with the following Jungle Scout API endpoints:

- `/api/v1/keywords/search` - Keyword search
- `/api/v1/products/search` - Product search
- `/api/v1/products/details` - Product details
- `/api/v1/keywords/analyze` - Keyword analysis
- `/api/v1/categories/search` - Category search
- `/api/v1/products/competitors` - Competitor analysis

For more information about the Jungle Scout API, visit: https://support.junglescout.com/hc/en-us/articles/21641823937943-API-Endpoint-Descriptions

## Error Handling

The server includes comprehensive error handling for:
- Invalid API keys
- Network errors
- Invalid parameters
- API rate limiting
- Server errors

All errors are returned in a structured JSON format with error details.

## Development

### Project Structure

```
jungle-scout-mcp/
├── main.py              # Main MCP server (production mode)
├── mcp_server.py        # FastMCP instance for Claude Desktop installation
├── dev_server.py        # Development server (with MCP Inspector)
├── requirements.txt     # Python dependencies
├── env.example         # Environment variables template
├── api/                # API client implementation
├── config/             # Configuration management
├── models/             # Pydantic models for requests
├── tools/              # Tool handlers
└── README.md          # This file
```

### Adding New Tools

To add new tools to the MCP server:

1. Add a new method to the `JungleScoutAPI` class
2. Create a corresponding Pydantic model for request validation
3. Add the tool definition to the `handle_list_tools()` function
4. Add the tool handler to the `handle_call_tool()` function

## License

This project is open source and available under the MIT License. 