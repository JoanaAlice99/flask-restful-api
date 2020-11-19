from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from config.db import db

#---Import Resources---
#from security import authenticate, identity
from resource.api import Home

app = Flask(__name__)
api = Api(app)

#--- Add Resources---
api.add_resource(Home, '/')

if __name__ == "__main__":
    db.connect()
    app.run(port=5000, debug=True)