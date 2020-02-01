from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from code.security import authenticate, identity
from code.resources.user import UserRegister
from code.resources.item import Item, ItemList
from code.resources.store_resource import StoreModel, Store

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from code.db import db
    db.init_app(app)
    app.run(port=5000)
