import requests
import json
from typing import List, Dict, Optional
import os
from datetime import datetime
from dotenv import load_dotenv

class N11CategoryFetcher:
    """
    N11 Turkey Marketplace Category Fetcher
    API Version: v7_30
    
    This class handles fetching categories and their attributes from the N11 Turkey Marketplace.
    Required API Credentials:
    - API Key (set in .env file or environment variables)
    - API Password (set in .env file or environment variables)
    
    Note: While this module focuses on category fetching, the same credentials can be used for:
    - Product Creation
    - APM (Automated Price Management)
    - Stock/Price Updates
    """
    
    def __init__(self, app_key: str):
        """
        Initialize the N11 Category Fetcher.
        
        Args:
            app_key (str): The N11 API key from .env file or environment variables.
        """
        self.app_key = app_key
        self.base_url = "https://api.n11.com/cdn"
        self.headers = {"appkey": self.app_key}
        
    def get_all_categories(self) -> Dict:
        """Fetch all categories from N11."""
        url = f"{self.base_url}/categories"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_category_attributes(self, category_id: str) -> Dict:
        """Fetch attributes for a specific category."""
        url = f"{self.base_url}/category/{category_id}/attribute"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def find_leaf_categories(self, category: Dict, leaf_categories: List[Dict] = None) -> List[Dict]:
        """Recursively find all leaf categories (categories with no subcategories)."""
        if leaf_categories is None:
            leaf_categories = []
            
        if category.get("subCategories") is None:
            leaf_categories.append({
                "id": category["id"],
                "name": category["name"],
                "fullName": category.get("fullName", category["name"])
            })
        else:
            for subcategory in category["subCategories"]:
                self.find_leaf_categories(subcategory, leaf_categories)
                
        return leaf_categories
    
    def process_all_categories(self) -> Dict:
        """Process all categories and their attributes."""
        # Get all categories
        print("Fetching all categories...")
        categories = self.get_all_categories()
        
        # Find all leaf categories
        print("Finding leaf categories...")
        leaf_categories = []
        for category in categories["categories"]:
            leaf_categories.extend(self.find_leaf_categories(category))
        
        # Get attributes for each leaf category
        print(f"Found {len(leaf_categories)} leaf categories. Fetching attributes...")
        result = {
            "timestamp": datetime.now().isoformat(),
            "categories": []
        }
        
        for idx, category in enumerate(leaf_categories, 1):
            print(f"Processing category {idx}/{len(leaf_categories)}: {category['name']}")
            try:
                attributes = self.get_category_attributes(category["id"])
                category_data = {
                    **category,
                    "attributes": attributes.get("categoryAttributes", [])
                }
                result["categories"].append(category_data)
            except Exception as e:
                print(f"Error processing category {category['name']}: {str(e)}")
        
        return result
    
    def save_results(self, data: Dict, filename: str = "n11_categories.json"):
        """Save the results to a JSON file."""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Results saved to {filename}")

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the app key from environment variable
    app_key = os.getenv("N11_APP_KEY")
    if not app_key:
        print("Please set the N11_APP_KEY environment variable in the .env file or export it in your shell")
        return
    
    fetcher = N11CategoryFetcher(app_key)
    try:
        results = fetcher.process_all_categories()
        fetcher.save_results(results)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 