from flask import Flask
from flask_jwt import JWT, jwt_required
from flask_restful import Api, Resource, reqparse

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "jose"
api = Api(app)
items = [{"name": "a", "price": 12.00}]
jwt = JWT(app, authenticate, identity)


class Student(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True,
                        help="can not leave blank")

    @jwt_required()
    # open postman and make first call to /auth post req mention content-type=application/json
    # and in body mentions { username: , password} , it creates a JWT
    def get(self, name):
        item = next(filter(lambda x: x == name, items), None)
        return item, 200 if item else 404

    def put(self, name):
        item = next(filter(lambda x: x == name, items), None)
        data = Student.parser.parse_args()
        if item is None:
            item = {"name": name, "price": data['price']}
            items.append(item)
        else:
            item.update(data)
        return item, 201 if item else 400


class ItemLi(Resource):

    def get(self):
        #request_data = request.get_json()
        return {"items": items}


api.add_resource(Student, '/item/<string:name>')
api.add_resource(ItemLi, '/items')
app.run()
