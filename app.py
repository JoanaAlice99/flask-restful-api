from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

#---Import Resources---
from config.security import authenticate, identity
from resource.api import Home
from resource.user import UserRegister

#---Flask App---
app = Flask(__name__)
api = Api(app)

#---JWT---
jwt = JWT(app, authenticate, identity)

#---Add Resources---
api.add_resource(Home, '/')
api.add_resource(UserRegister, '/user/register')

if __name__ == "__main__":
    app.run(port=4000, debug=True)