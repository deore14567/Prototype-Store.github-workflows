from flask import Flask, jsonify, render_template, request
from amazon_scraper import search_amazon
from flipkart_scraper import search_flipkart
from myntra_scraper import search_myntra
from product_library import store_product_data, fetch_product_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search_product():
    product_name = request.json.get("product_name")
    if not product_name:
        return jsonify({"error": "No product name provided"}), 400

    amazon_data = search_amazon(product_name)
    flipkart_data = search_flipkart(product_name)
    myntra_data = search_myntra(product_name)

    store_product_data(product_name, amazon_data["price"], "Amazon")
    store_product_data(product_name, flipkart_data["price"], "Flipkart")
    store_product_data(product_name, myntra_data["price"], "Myntra")

    product_data = fetch_product_data(product_name)
    all_prices = product_data.get("platform_prices", [])
    best_price_data = min(all_prices, key=lambda x: x["price"])

    return jsonify({
        "product_name": product_name,
        "best_price": best_price_data["price"],
        "best_platform": best_price_data["platform"],
        "all_prices": all_prices
    })

if __name__ == '__main__':
    app.run(debug=True)
