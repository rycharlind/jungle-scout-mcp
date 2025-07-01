from pydantic import BaseModel, Field


class KeywordSearchRequest(BaseModel):
    keyword: str = Field(..., description="The keyword to search for")
    marketplace: str = Field(
        default="US", description="Marketplace (US, CA, UK, DE, FR, IT, ES, JP, IN, MX, AU, BR)")
    page: int = Field(default=1, description="Page number for pagination")
    page_size: int = Field(
        default=20, description="Number of results per page")


class ProductSearchRequest(BaseModel):
    query: str = Field(..., description="Product search query")
    marketplace: str = Field(
        default="US", description="Marketplace (US, CA, UK, DE, FR, IT, ES, JP, IN, MX, AU, BR)")
    page: int = Field(default=1, description="Page number for pagination")
    page_size: int = Field(
        default=20, description="Number of results per page")


class ProductDetailsRequest(BaseModel):
    asin: str = Field(..., description="Amazon ASIN of the product")
    marketplace: str = Field(
        default="US", description="Marketplace (US, CA, UK, DE, FR, IT, ES, JP, IN, MX, AU, BR)")


class KeywordAnalyzerRequest(BaseModel):
    keyword: str = Field(..., description="The keyword to analyze")
    marketplace: str = Field(
        default="US", description="Marketplace (US, CA, UK, DE, FR, IT, ES, JP, IN, MX, AU, BR)")


class CategorySearchRequest(BaseModel):
    query: str = Field(..., description="Category search query")
    marketplace: str = Field(
        default="US", description="Marketplace (US, CA, UK, DE, FR, IT, ES, JP, IN, MX, AU, BR)")


class CompetitorAnalysisRequest(BaseModel):
    asin: str = Field(..., description="Amazon ASIN of the product")
    marketplace: str = Field(
        default="US", description="Marketplace (US, CA, UK, DE, FR, IT, ES, JP, IN, MX, AU, BR)")
