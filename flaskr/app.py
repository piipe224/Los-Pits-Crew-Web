from . import db
from flask import request, make_response
from . import app
from .models import User, Address
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta, timezone
from functools import wraps
import jwt


@app.route("/signup", methods=["POST"])

def signup():
    data = request.json
    type_identification = data.get("type_identification")
    number_identification = data.get("number_identification")
    name = data.get("name")
    last_name = data.get("last_name")
    id_rol = data.get("id_rol")
    cell_phone = data.get("cell_phone")
    email = data.get("email")
    password = data.get("password")

    if type_identification and number_identification and name and last_name and id_rol and cell_phone and email and password:
        user = User.query.filter_by(email=email, number_identification=number_identification).first()
        if user: 
            return make_response(
                {"Mensaje": "Parece que ya tienes un usuario creado con el correo que ingresaste o con tu numero de identificacion. Por favor Inicia sesion."},
                200
            )
        user = User(
            type_identification = type_identification,
            number_identification = number_identification,
            name = name,
            last_name = last_name,
            id_rol = id_rol,
            cell_phone = cell_phone,
            email = email,
            password = generate_password_hash(password)
        )

        db.session.add(user)
        db.session.commit()

        return make_response(
            {"Mensaje": "Usuario creado exitosamente"},
            201
        )

    return make_response(
        {"Error": "Algo fallo en la creacion del usuario"},
        500
    )

@app.route("/login", methods=["POST"])

def login():

    auth = request.json
    if not auth or not auth.get("email") or not auth.get("password"):
        return make_response(
            "Diligencia los datos requeridos para poder iniciar sesion",
            401
        )
    user = User.query.filter_by(email = auth.get("email")).first()
    if not user:
        return make_response(
            "Registrate primero, para que puedas iniciar sesion y disfrutar de nuestros servicios"
        )
    if check_password_hash(user.password, auth.get('password')):
        token = jwt.encode({
            'id_user': user.id_user,
            'token_exp': (datetime.now(timezone.utc) + timedelta(minutes=30)).isoformat()
        },
        "secret",
        "HS256"
        )

        return make_response({'Token': token}, 201)
    
    return make_response(
        "Por favor verifica tus credenciales"
    )

def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return make_response({"Mensaje": "No se encuentra el Token"}, 401)

        try:
            data = jwt.decode(token, "secret", algorithms=["HS256"])
            current_user = User.query.filter_by(id = data["id_user"]).first()
            print(current_user)
        except Exception as e:
            print(e)
            return make_response({
                "Error": "El Token es invalido"
            }, 
            401
            )
        return f(current_user, *args, **kwargs)
    return decorated