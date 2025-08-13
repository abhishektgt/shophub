from flask import Blueprint, request, jsonify
from database import products

products_bp = Blueprint('products', __name__)

@products_bp.route("/products", methods=["GET"])
def get_products():
    try:
        category = request.args.get('category')
        brand = request.args.get('brand')
        
        query = {}
        if category:
            query['category'] = category
        if brand:
            query['brand'] = brand
            
        products_list = list(products.find(query))
        return jsonify(products_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@products_bp.route("/products/<product_id>", methods=["GET"])
def get_product(product_id):
    try:
        product = products.find_one({"_id": product_id})
        if not product:
            return jsonify({"error": "Product not found"}), 404
        return jsonify(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500