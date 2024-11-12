import requests
from bs4 import BeautifulSoup

def search_flipkart(product_name):
    search_url = f"https://www.flipkart.com/search?q={product_name.replace(' ', '%20')}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    product = soup.find("a", {"class": "s1Q9rs"})
    price = soup.find("div", {"class": "_30jeq3"})

    if product and price:
        return {
            "platform": "Flipkart",
            "name": product.text.strip(),
            "price": float(price.text.replace("₹", "").replace(",", ""))
        }
    return {"error": "Product not found"}
