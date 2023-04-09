from flask import Flask,jsonify,request,render_template
from pymongo import MongoClient
from bson import json_util,ObjectId
from flask_cors import CORS
from flask_bcrypt import Bcrypt
import os
import json
from dotenv import load_dotenv


# Carga las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

# Conexion con la Base De Datos
mongo_uri = os.environ.get('MONGO_URL')
client = MongoClient(mongo_uri)
db = client.crud_flask


@app.route('/')
def Index():
    return render_template('index.html')



@app.route('/api/Agregar', methods=["POST"])
def Agregar():
    name = request.json['Nombre']
    email = request.json['Email']
    password = request.json['Password']
    # Enviar Datos recibidos desde el cliente
    if name and email and password:
        pw_hash = bcrypt.generate_password_hash(password)
        _id = db.datos.insert_one({'Nombre': name, 'Email': email, 'Password': pw_hash})
        return jsonify({'_id': str(_id.inserted_id), 'Nombre': name, 'Password': str(pw_hash)})
    else:
        return "no fue posible enviar"


# Una busqueda mas especifica por ID o puede ser algun dato que tengamos en la base de datos. puede ser el Nombre tambien el find_one nos arrojara los resultados que hagan coincidencia con lo que le pasemos
@app.route('/api/Buscar/<id>', methods=["GET"])
def Buscar(id):
    # Enviar Datos recibidos desde el cliente
        result = list(db.datos.find({'_id': ObjectId(id)}))
        output = json.loads(json_util.dumps(result))
        return jsonify(output)


# Para obtener todo los datos sin filtro bastaria solo cambiar el find_one a Find 
@app.route('/api/Todo', methods=["GET"])
def BuscarTodo():
    # Enviar Datos recibidos desde el cliente
        result = list(db.datos.find({}))
        output = json.loads(json_util.dumps(result))
        return jsonify({"Datos": output})



# Desde el cliente enviamos el id. para entonces mediante un Dele_one pueda elimianr el documento que coincida con el ID que enviamos
@app.route('/api/Eliminar/<id>', methods=["DELETE"])
def Eliminar(id):
    # Enviar Datos recibidos desde el cliente
        db.datos.delete_one({'_id': ObjectId(id)})
        response = jsonify({"mensaje": "Registro con: " + id + "" " Fue eliminado"})
        return response







if __name__ == '__main__':
    app.run(debug=True)