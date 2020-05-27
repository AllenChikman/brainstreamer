"""
Exposing the results in a Gui.
Backend: Flask and jinja templates
FrondEnd: JS, Query, ajax, html, css
"""
import os

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
api_url = ""


def run_website(host, port, api_address):
    global api_url
    api_url = api_address
    app.run(host, int(port))


@app.route('/')
def index():
    return render_template('index.html', api_url=api_url)


@app.route('/users')
def users():
    return render_template('users.html', api_url=api_url)


@app.route('/users/<user_id>/snapshots')
def snapshots(user_id):
    return render_template('snapshots.html', user_id=user_id, api_url=api_url)


@app.route('/users/<user_id>/snapshots/<snapshot_id>')
def result_middleman(user_id, snapshot_id):
    return render_template('results.html', user_id=user_id, snapshot_id=snapshot_id, api_url=api_url)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
