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


@app.route('/snapshots/<user_id>')
def snapshots(user_id):
    return render_template('snapshots.html', user_id=user_id)


@app.route('/results/<snapshot_id>')
def results(snapshot_id):
    return render_template('results.html', snapshot_id=snapshot_id)


####### Refrences


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return send_from_directory('.', 'index.html')
    # return render_template('index2.html', name=name)

