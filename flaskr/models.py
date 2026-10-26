from . import db
from sqlalchemy.sql import func

#Conexion con la tabla de rol de la base de datos

class Rol(db.Model):

    __tablename__="rol"
    __table_args__={"schema": "data_users"}

    id_rol = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(20), nullable=False)
    user = db.relationship('User', backref="Rol")

    def __repr__(self):
        return f'<Roles {self.id_rol} {self.rol}'

#Conexion con la tabla de usuario de la base de datos

class User(db.Model):

    __tablename__="user"
    __table_args__={"schema": "data_users"}

    id_user = db.Column(db.BigInteger, primary_key=True)
    type_identification = db.Column(db.String(30), nullable=False)
    number_identification = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    id_rol = db.Column(db.Integer, db.ForeignKey("data_users.rol.id_rol"))
    cell_phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(350), nullable=False)
    create_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    address = db.relationship('Address', backref="User")
    rol = db.relationship('Rol', backref="User")

    def __repr__(self):
        return f'<User {self.name} {self.id_user}'

#Conexion con la tabla de direcciones

class Address(db.Model):

    __tablename__="address"
    __table_args__={"schema": "data_users"}

    id_address = db.Column(db.BigInteger, primary_key=True)
    id_user = db.Column(db.BigInteger, db.ForeignKey("data_users.user.id_user"), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    municipality = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    neighborhood = db.Column(db.String(30), nullable=False)
    main_street = db.Column(db.String(20), nullable=False)
    n_main_street = db.Column(db.Integer, nullable=False)
    l_main_street = db.Column(db.String(1), nullable=False)
    bis_street = db.Column(db.Boolean, nullable=False)
    n_cmpltary = db.Column(db.Integer, nullable=False)
    l_cmpltary = db.Column(db.String(1), nullable=False)
    bis_cmpltary = db.Column(db.Boolean, nullable=False)
    num_dst = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    user = db.relationship('User', backref="Address")