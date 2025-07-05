from api.jungle_scout import JungleScoutAPI
from config.constants import PRODUCT_SEARCH_LIMIT
from tools.handlers import create_tool_handler
from models.requests.product_search import ProductSearchRequest


def create_search_products_tool(api_client: JungleScoutAPI):
    """Create and return the search_products tool function"""
    
    # Use the generic handler pattern
    tool_handler = create_tool_handler(
        request_model_class=ProductSearchRequest,
        api_method_name="search_products",
        api_client=api_client,
        additional_params={"page_size": PRODUCT_SEARCH_LIMIT}
    )
    
    async def search_products(**kwargs):
        """Search for products on Amazon with advanced filtering options including product tiers, seller types, keyword inclusion/exclusion, price ranges, sales metrics, review metrics, and weight ranges
        
        Parameters:
        - marketplace: Marketplace (US, CA, UK, DE, FR, IT, ES, JP, IN, MX, AU, BR)
        - page: Page number for pagination
        - product_tiers: Product tiers to include (oversize, standard, etc.)
        - seller_types: Seller types to include (amz, fba, fbm)
        - include_keywords: Keywords that must be included in product listings
        - exclude_keywords: Keywords to exclude from product listings
        - exclude_top_brands: Whether to exclude top brands
        - exclude_unavailable_products: Whether to exclude unavailable products
        - min_price/max_price: Price range filters
        - min_net/max_net: Net price range filters
        - min_rank/max_rank: Ranking range filters
        - min_sales/max_sales: Sales metrics filters
        - min_revenue/max_revenue: Revenue filters
        - min_reviews/max_reviews: Review count filters
        - min_rating/max_rating: Rating filters (1-5 scale)
        - min_weight/max_weight: Weight range filters
        """
        return await tool_handler(**kwargs)
    
    return search_products 