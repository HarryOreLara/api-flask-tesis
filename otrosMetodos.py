
from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from product import Product
from analisis import Analisis


db = dbase.dbConnection()

app = Flask(__name__)

# Method Post
@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    product_data = request.get_json()

    name = product_data['name']
    price = product_data['price']
    quantity = product_data['quantity']

    if name and price and quantity:
        product = Product(name, price, quantity)
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'status': 'success' if product else 'failure'
        })
        return response
    else:
        return notFound()
    


# Method delete
@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = db['products']
    products.delete_one({'name': product_name})
    return redirect(url_for('home'))

# Method Put
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    products = db['products']
    product_data = request.get_json()

    name = product_data['name']
    price = product_data['price']
    quantity = product_data['quantity']

    if name and price and quantity:
        products.update_one({'name': product_name}, {'$set': {'name': name, 'price': price, 'quantity': quantity}})
        response = jsonify({'message': 'Producto ' + product_name + ' actualizado correctamente'})
        return response
    else:
        return notFound()
    

    
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response
