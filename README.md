# N11 Category Fetcher (Turkey Marketplace)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

A Python tool for fetching and managing product categories from the N11 Turkey Marketplace API. This tool helps e-commerce integrators and sellers to:

1. Retrieve the complete category tree from N11
2. Identify leaf categories (categories with no subcategories)
3. Fetch attributes for each category
4. Save all data in a structured JSON format

## Features

- 🌳 Complete category tree traversal
- 📝 Detailed attribute information for each category
- 🔍 Identification of mandatory and variant attributes
- 💾 JSON output for easy integration
- ⚡ Efficient API usage with proper error handling
- 🔒 Secure credential management

## Prerequisites

- Python 3.6 or higher
- N11 Marketplace API credentials
- Basic understanding of N11's API structure

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/n11-category-fetcher.git
cd n11-category-fetcher
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create your environment file:
```bash
cp .env.example .env
```

4. Edit `.env` with your N11 API credentials:
```bash
N11_APP_KEY="your_api_key_here"
N11_API_PASSWORD="your_api_password_here"
```

## Usage

Simply run the main script:
```bash
python n11_category_fetcher.py
```

The script will:
1. Connect to N11's API
2. Fetch all categories
3. Process each category's attributes
4. Save the results to `n11_categories.json`

## Output Format

The output JSON file follows this structure:
```json
{
  "timestamp": "2024-03-XX:XX:XX.XXXXX",
  "categories": [
    {
      "id": "category_id",
      "name": "category_name",
      "fullName": "full_category_path",
      "attributes": [
        {
          "id": "attribute_id",
          "name": "attribute_name",
          "isMandatory": true/false,
          "isVariant": true/false,
          "values": [
            {
              "id": "value_id",
              "value": "value_name"
            }
          ]
        }
      ]
    }
  ]
}
```

## Important Notes

- Only leaf categories (categories with no subcategories) are processed for attributes
- The script handles rate limiting and errors gracefully
- Progress is displayed in the console during execution
- This integration is specifically for N11 Turkey Marketplace
- Supports Product Creation, APM, and Stock/Price updates (through separate modules)
- Based on N11 SOAP API Documentation v7_30

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- N11 Marketplace for providing the API
- All contributors to this project

## Support

If you encounter any problems or have questions, please [open an issue](https://github.com/your-username/n11-category-fetcher/issues). 