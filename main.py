#imported modules
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class hello_world(Resource):
    def post(self):
        post_received = request.get_json()
        text_received = post_received['txt']
        return {'response':[text_received,'hello again']}


api.add_resource(hello_world, '/api/nlp')

if __name__ == "__main__":
    app.run(debug=True)