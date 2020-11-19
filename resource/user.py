from flask_restful import Resource, reqparse

from model.user import UserModel
user_model = UserModel()

#User Register
class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self):
        user = UserRegister.parser.parse_args()
        print(user["username"])

        if user_model.find_by_username(user["username"]):
            return {
                "message": "The user already exists"
            }
        #else:
        #    UserModel.save(user)
        

