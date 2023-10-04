# PORT=3000

# DB_CONNECTION = mongodb+srv://harry:root@cluster0.aniauvv.mongodb.net/dicta?retryWrites=true&w=majority
# KEY_SECRET = 167361711002


#python -m pip install pymongo==3.11
#pip install certifi
#pip install pymongo[srv]

from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://harry:root@cluster0.aniauvv.mongodb.net/?retryWrites=true&w=majority'

ca = certifi.where()


def dbConnection():
    try:
        client = MongoClient.connect(MONGO_URI, tlsCAFile=ca)
        db = client["db_products"]
    except ConnectionError:
        print("Error de conexion con la base de datos")
    
    return db