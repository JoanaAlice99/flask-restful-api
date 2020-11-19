from flask_restful import Resource
from datetime import datetime

class Home(Resource):

    # API Info Endpoints

    def get(self):
        return {
            "API": {
                "name": "flask TODO RESTful API",
                "ver": "1.0",
                "date": str(datetime.now())
            }
        }