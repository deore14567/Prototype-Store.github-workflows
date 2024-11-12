import json
from datetime import datetime

def store_product_data(product_name, price, platform):
    try:
        with open('product_library.json', 'r') as f:
            products = json.load(f)
    except FileNotFoundError:
        products = {}

    if product_name not in products:
        products[product_name] = {"price_history": [], "platform_prices": []}

    products[product_name]["price_history"].append({
        "date": datetime.now().isoformat(),
        "price": price
    })

    products[product_name]["platform_prices"].append({
        "platform": platform,
        "price": price,
        "date": datetime.now().isoformat()
    })

    with open('product_library.json', 'w') as f:
        json.dump(products, f, indent=4)

def fetch_product_data(product_name):
    try:
        with open('product_library.json', 'r') as f:
            products = json.load(f)
        return products.get(product_name, {})
    except FileNotFoundError:
        return {}
