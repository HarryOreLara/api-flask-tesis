from flask import Flask, render_template
import database as dbase
from product import Product


app = Flask(__name__)






#Rutas de la aplicacion
@app.route('/')
def home():
    return render_template('index.html')






if __name__ == '__main___':
    app.run(debug=True, port=5000)