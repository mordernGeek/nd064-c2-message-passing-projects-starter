from flask import Flask, jsonify 
from flask_restx import Namespace, Resource
import logging

api = Namespace("UdaConnect", description="REST API endpoint")

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")

@api.route("/new", methods=['GET'])

def health():
    return jsonify({'result': 'Flask Endpoint check!'})