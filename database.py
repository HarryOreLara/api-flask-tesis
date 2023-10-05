# PORT=3000

# DB_CONNECTION = mongodb+srv://harry:root@cluster0.aniauvv.mongodb.net/dicta?retryWrites=true&w=majority
# KEY_SECRET = 167361711002


#python -m pip install pymongo==3.11
#pip install certifi
#pip install pymongo[srv]

from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://mdDicta2023:YtTQsy7uWbkKyR7U@dicta.3pwgqtl.mongodb.net/bddictacolombia?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db