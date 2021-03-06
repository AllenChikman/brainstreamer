"""
This module runs a server with REST API and responses with the saved data from the provided DB.
"""

from flask import Flask, jsonify, send_file
from brainstreamer.platforms.databases import DBWrapper

serv = Flask(__name__)
db = None


# Run the server on the given address using the provided DB
def run_api_server(host, port, database_url):
    global db
    db = DBWrapper(database_url)
    serv.run(host, int(port))


# Wraps the response with json format and adds an header to it
def _wrap_response(data):
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@serv.route('/users', methods=['GET'])
def get_users():
    users = db.get_users()
    users = [{'user_id': user['user_id'], 'username': user['username']} for user in users]
    return _wrap_response(users)


@serv.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    user = db.get_user_by_id(user_id)
    return _wrap_response(user)


@serv.route('/users/<int:user_id>/snapshots')
def get_snapshots_by_user_id(user_id):
    snapshots = db.get_snapshots_by_user_id(user_id)
    snapshots = [{'snapshot_id': snapshot['snapshot_id'], 'datetime': snapshot['datetime']}
                 for snapshot in snapshots]
    return _wrap_response(snapshots)


@serv.route('/users/<int:user_id>/snapshots/<snapshot_id>')
def get_snapshot_by_id(user_id, snapshot_id):
    snapshot = db.get_snapshot_by_id(user_id, snapshot_id)
    results = list(snapshot['results'].keys())
    return _wrap_response(results)


@serv.route('/users/<int:user_id>/snapshots/<snapshot_id>/<result_name>')
def get_snapshot_result(user_id, snapshot_id, result_name):
    result = db.get_snapshot_by_id(user_id, snapshot_id)['results'][result_name]
    return _wrap_response(result)


@serv.route('/users/<int:user_id>/snapshots/<snapshot_id>/<result_name>/data')
def get_snapshot_result_data(user_id, snapshot_id, result_name):
    path = db.get_snapshot_by_id(user_id, snapshot_id)['results'][result_name]['data_path']
    return send_file(path)
