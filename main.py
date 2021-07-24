#imported modules
from flask import Flask, request
from flask_restful import Resource, Api
from word_combination import return_token_combi
from JSON_handler import add_api_to_json

app = Flask(__name__)
api = Api(app)

class hello_world(Resource):
    def post(self):
        post_received = request.get_json()
        text_received = post_received['txt']
        combi = return_token_combi(text_received)
        return {'response':combi}

class add_api(Resource):
    def post(self):
        post_received = request.get_json()
        api_name = post_received['name']
        api_data = post_received['body']
        add_api_to_json('./data/API_collection.json', api_name, api_data)
        return 'added API!'

api.add_resource(add_api,'/api/add')
api.add_resource(hello_world, '/api/nlp')

if __name__ == "__main__":
    app.run(debug=True)