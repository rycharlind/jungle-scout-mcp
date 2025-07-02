from pydantic import BaseModel, Field, field_validator
from typing import List, Optional


class ProductSearchRequest(BaseModel):
    marketplace: str = Field(
        default="us",
        description="Marketplace (US, CA, UK, DE, FR, IT, ES, JP, IN, MX, AU, BR)",
    )
    page: int = Field(default=1, description="Page number for pagination")

    # Product tiers and seller types
    product_tiers: Optional[List[str]] = Field(
        default=None,
        description="Product tiers to include (oversize, standard, etc.)"
    )
    seller_types: Optional[List[str]] = Field(
        default=None,
        description="Seller types to include (amz, fba, fbm)"
    )

    # Keyword filtering
    include_keywords: Optional[List[str]] = Field(
        default=None,
        description="Keywords that must be included in product listings"
    )
    exclude_keywords: Optional[List[str]] = Field(
        default=None,
        description="Keywords to exclude from product listings"
    )

    # Exclusion flags
    exclude_top_brands: Optional[bool] = Field(
        default=None,
        description="Whether to exclude top brands"
    )
    exclude_unavailable_products: Optional[bool] = Field(
        default=None,
        description="Whether to exclude unavailable products"
    )

    # Price ranges
    min_price: Optional[float] = Field(
        default=None,
        description="Minimum price filter"
    )
    max_price: Optional[float] = Field(
        default=None,
        description="Maximum price filter"
    )
    min_net: Optional[float] = Field(
        default=None,
        description="Minimum net price filter"
    )
    max_net: Optional[float] = Field(
        default=None,
        description="Maximum net price filter"
    )

    # Ranking ranges
    min_rank: Optional[int] = Field(
        default=None,
        description="Minimum rank filter"
    )
    max_rank: Optional[int] = Field(
        default=None,
        description="Maximum rank filter"
    )

    # Sales metrics
    min_sales: Optional[int] = Field(
        default=None,
        description="Minimum sales filter"
    )
    max_sales: Optional[int] = Field(
        default=None,
        description="Maximum sales filter"
    )
    min_revenue: Optional[float] = Field(
        default=None,
        description="Minimum revenue filter"
    )
    max_revenue: Optional[float] = Field(
        default=None,
        description="Maximum revenue filter"
    )

    # Review metrics
    min_reviews: Optional[int] = Field(
        default=None,
        description="Minimum number of reviews filter"
    )
    max_reviews: Optional[int] = Field(
        default=None,
        description="Maximum number of reviews filter"
    )
    min_rating: Optional[float] = Field(
        default=None,
        description="Minimum rating filter (1-5 scale)"
    )
    max_rating: Optional[float] = Field(
        default=None,
        description="Maximum rating filter (1-5 scale)"
    )

    # Weight ranges
    min_weight: Optional[float] = Field(
        default=None,
        description="Minimum weight filter"
    )
    max_weight: Optional[float] = Field(
        default=None,
        description="Maximum weight filter"
    )

    @field_validator('marketplace')
    @classmethod
    def normalize_marketplace(cls, v):
        """Normalize marketplace to lowercase"""
        if v is None:
            return "us"
        return v.lower()

    @field_validator('page', 'min_rank', 'max_rank', 'min_sales', 'max_sales', 'min_reviews', 'max_reviews')
    @classmethod
    def parse_int_fields(cls, v):
        """Parse integer fields that might come as strings"""
        if v is None:
            return v
        if isinstance(v, int):
            return v
        if isinstance(v, str):
            try:
                return int(float(v))
            except (ValueError, TypeError):
                return v
        return v

    @field_validator('min_price', 'max_price', 'min_net', 'max_net', 'min_revenue', 'max_revenue', 'min_rating', 'max_rating', 'min_weight', 'max_weight')
    @classmethod
    def parse_float_fields(cls, v):
        """Parse float fields that might come as strings"""
        if v is None:
            return v
        if isinstance(v, (int, float)):
            return float(v)
        if isinstance(v, str):
            try:
                return float(v)
            except (ValueError, TypeError):
                return v
        return v

    @field_validator('exclude_top_brands', 'exclude_unavailable_products')
    @classmethod
    def parse_bool_fields(cls, v):
        """Parse boolean fields that might come as strings"""
        if v is None:
            return v
        if isinstance(v, bool):
            return v
        if isinstance(v, str):
            return v.lower() in ('true', '1', 'yes', 'on')
        return bool(v)
