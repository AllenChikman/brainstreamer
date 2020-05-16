from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, send_from_directory
from markupsafe import escape

app = Flask(__name__)


def run_website(host, port):
    app.run(host, int(port))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def users():
    return render_template('users.html')


@app.route('/users/<user_id>/snapshots')
def snapshots(user_id):
    return render_template('snapshots.html', user_id=user_id)


@app.route('/users/<user_id>/snapshots/<snapshot_id>')
def result_middleman(user_id, snapshot_id):
    return render_template('results.html', user_id=user_id, snapshot_id=snapshot_id)
