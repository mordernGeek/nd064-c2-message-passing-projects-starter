from flask import Flask, jsonify 
from flask_restx import Namespace, Resource
import logging

#api = Namespace("UdaConnect", description="REST API endpoint")
app = Flask(__name__)

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")

@app.route("/grpc", methods=['GET'])

def health():
    return jsonify({'result': 'Flask Endpoint check!'})