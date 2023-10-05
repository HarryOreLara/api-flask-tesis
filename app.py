from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from analisis import Analisis


db = dbase.dbConnection()

app = Flask(__name__)


# Rutas de la aplicación
@app.route('/')
def home():
    products = db['products']
    productsReceived = products.find()
    return render_template('index.html', products=productsReceived)


@app.route("/analisis", methods=['POST'])
def addMessage():
    analisis = db['analisis']
    analisis_data = request.get_json()

    idPersona = analisis_data['idPersona']
    nombre = analisis_data['nombre']
    frase = analisis_data['frase']
    fecha = analisis_data['fecha']
    ##PReparado para recibir el mensaje de procesmiento de la red neuronal
    estado_animo = "Enojado"

    if idPersona and nombre and frase and fecha and estado_animo:
        analis = Analisis(idPersona, nombre, frase, fecha, estado_animo)
        analisis.insert_one(analis.toDBCollection())
        response = jsonify({
            'status': 'success' if analis else 'failure'
        })
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


if __name__ == '__main___':
    app.run(debug=True, port=4000)
