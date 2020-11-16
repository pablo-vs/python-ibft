from flask import Flask, json, request, make_response, jsonify

import requests
import _thread, threading

from . import ibft


def message_primitive(dest_party, msg):
    _thread.start_new_thread(send_message, (dest_party["url"] + message_endpoint, msg))

def send_message(url, msg):
    try:
        requests.post(url, json=msg)
    except:
        pass


def run_server(port):
    _thread.start_new_thread(lambda: api.run(port=port, threaded=False, processes=1), ())

api = Flask(__name__)

message_endpoint = '/message'

def define_api(ibft_message_queue, ibft_instances, ibft_parties, ibft_id):

    @api.route(message_endpoint, methods=['POST'])
    def post_message():
        wrapped_message = request.json
        ibft_message_queue.put(wrapped_message)
        return make_response(jsonify(True), 200)

    @api.route('/instances', methods=['GET'])
    def get_instances():
        return make_response(jsonify(ibft_instances), 200)

    @api.route('/instance/<int:instance_id>/', methods=['GET'])
    def get_instance(instance_id):
        return make_response(jsonify(ibft_instances[instance_id]), 200)

    @api.route('/online', methods=['GET'])
    def get_online():
        return make_response(jsonify(True), 200)

    @api.route('/parties', methods=['GET'])
    def get_parties():
        return make_response(jsonify(ibft_parties), 200)

    @api.route('/id', methods=['GET'])
    def get_id():
        return make_response(jsonify(ibft_id), 200)


def start_ibft(privkey_json, parties_json, config_json, ibft_id):
    
    """
        Run this to configure the server, then call ibft.start_instance()
    """

    ibft.load_config(parties_json, config_json, privkey_json, ibft_id, message_primitive)
    define_api(ibft.ibft_message_queue, ibft.ibft_instances, ibft.ibft_parties, ibft_id)

    ibft.run_server()
    run_server(parties_json[ibft_id]["port"])
