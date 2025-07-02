#!/usr/bin/env python3
"""
Test script to verify the Jungle Scout API request fixes
"""

import asyncio
import json
from api.jungle_scout import JungleScoutAPI
from config.env import get_api_key

async def test_request():
    """Test the exact request that was failing"""
    
    # Your original request parameters
    test_params = {
        "page": 1,
        "max_price": "100",
        "min_price": "20", 
        "page_size": 50,
        "min_rating": "4.0",
        "marketplace": "US",
        "min_reviews": "100",
        "seller_types": '["FBA"]',
        "include_keywords": '["organic"]',
        "exclude_top_brands": "true"
    }
    
    print("Testing with original request parameters:")
    print(json.dumps(test_params, indent=2))
    print("\n" + "="*50 + "\n")
    
    try:
        # Initialize API client
        api_key = get_api_key()
        api_client = JungleScoutAPI(api_key)
        
        # Call the search_products method with the test parameters
        result = await api_client.search_products(
            marketplace=test_params["marketplace"],
            page=test_params["page"],
            page_size=test_params["page_size"],
            max_price=test_params["max_price"],
            min_price=test_params["min_price"],
            min_rating=test_params["min_rating"],
            min_reviews=test_params["min_reviews"],
            seller_types=test_params["seller_types"],
            include_keywords=test_params["include_keywords"],
            exclude_top_brands=test_params["exclude_top_brands"]
        )
        
        print("✅ SUCCESS! API call completed successfully.")
        print("\nResponse:")
        print(json.dumps(result, indent=2))
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_request()) 