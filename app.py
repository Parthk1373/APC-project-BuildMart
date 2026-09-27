from flask import Flask 
from flask import render_template

app = Flask(__name__)
products = [
    {"name": "Plywood", "category": "plywood", "price": 1200},
    {"name": "Cement Bag", "category": "cement", "price": 380},
    {"name": "Cement Tile", "category": "Tiles", "price": 45},
]

@app.route('/')
def home():
    return "Welcome to BuildMArt"

@app.route('/products')
def product_page():
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)

