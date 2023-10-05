from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from analisis import Analisis


db = dbase.dbConnection()

app = Flask(__name__)


@app.route("/analisis", methods=['POST'])
def addMessage():
    analisis = db['analisis']
    analisis_data = request.get_json()

    idPersona = analisis_data['idPersona']
    nombre = analisis_data['nombre']
    mensaje = analisis_data['mensaje']
    fecha = analisis_data['fecha']

    if idPersona and nombre and mensaje and fecha:
        analis = Analisis(idPersona, nombre, mensaje, fecha)
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
