from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from analisis import Analisis
import os
import keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pickle


db = dbase.dbConnection()

app = Flask(__name__)

########################################


model = keras.models.load_model('redes_neuronales.h5')
# Carga el codificador de etiquetas
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))
tokenizer = pickle.load(open('tokenizer.pkl', 'rb'))
# Función de preprocesamiento de texto
def preprocess_text(text):
    # Conversión a minúsculas
    text = text.lower()

    # Eliminación de caracteres especiales y puntuación
    text = re.sub(r'[^\w\s]', '', text)

    return text

########################################


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
    frase_body = analisis_data['frase']
    fecha = analisis_data['fecha']
    ##PReparado para recibir el mensaje de procesmiento de la red neuronal
    #estado_animo = "Enojado"

    analizando = frase_body
    analizando = preprocess_text(analizando)
    maxlen =30
    analizando_sequence = tokenizer.texts_to_sequences([analizando])
    analizando_sequence = pad_sequences(analizando_sequence, maxlen=maxlen)

    #PRediccion de dentimiento
    prediccion = model.predict(analizando_sequence)
    prediccion_clase = np.argmax(prediccion, axis=-1)

    clase_predicha = label_encoder.inverse_transform(prediccion_clase)

    frase = frase_body
    estado_animositos = clase_predicha[0]
    estado_animo = str(estado_animositos)









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
