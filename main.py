#imported modules
from flask import Flask, request
from flask_restful import Resource, Api
from word_combination import return_token_combi
app = Flask(__name__)
api = Api(app)

class hello_world(Resource):
    def post(self):
        post_received = request.get_json()
        text_received = post_received['txt']
        combi = return_token_combi(text_received)
        return {'response':combi}


api.add_resource(hello_world, '/api/nlp')

if __name__ == "__main__":
    app.run(debug=True)