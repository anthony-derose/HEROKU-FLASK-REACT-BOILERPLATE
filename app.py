from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from api.api_handler import api_handler

app = Flask(__name__, static_url_path='', static_folder='frontend/build/')
#cors = CORS(app)
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(api_handler, '/test')

if __name__ == "__main__":
    app.run(host='0.0.0.0')