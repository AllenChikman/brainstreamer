from pathlib import Path
import datetime as dt
import os
from flask import Flask


data_path = ""
website = Flask(__name__)


def get_relevant_timestamp_format(timestamp):
    temp_str = timestamp.replace(".txt", "")
    return dt.datetime.strptime(temp_str, '%Y-%m-%d_%H-%M-%S')


@website.route('/users/<int:user_id>')
def user(user_id):
    _USER_HTML = '''
    <html>
        <head>
            <title>Brain Computer Interface: User {user_id}</title>
        </head>
            <body>
            <table>
                {user_thoughts}
            </table>
        </body>
    </html>
    '''
    _THOUGHT_LINE_HTML = '''
                <tr>
                    <td>{file_name}</td>
                    <td>{thought}</td>
                </tr> 
                '''

    cur_path = f'{str(data_path)}/{user_id}'
    users_thoughts_lines = []

    if not os.path.exists(cur_path):
        return

    for file_dir in Path(cur_path).iterdir():
        file_name = get_relevant_timestamp_format(file_dir.name)
        thought = open(file_dir).read()
        users_thoughts_lines.append(_THOUGHT_LINE_HTML.format(file_name=file_name, thought=thought))
    user_html = _USER_HTML.format(user_id=user_id, user_thoughts='\n'.join(users_thoughts_lines))

    return user_html


@website.route('/')
def index():
    _INDEX_HTML = '''
    <html>
        <link rel="icon" href="data:;base64,iVBORw0KGgo=">
        <head>
            <title>Brain Computer Interface</title>
        </head>
        <body>
            <ul>
                {users}
            </ul>
        </body>
    </html>
    '''
    _USER_LINE_HTML = '''
    <li><a href="/users/{user_id}">user {user_id}</a></li>
    '''

    users_html = []
    for user_dir in Path(data_path).iterdir():
        users_html.append(_USER_LINE_HTML.format(user_id=user_dir.name))
    index_html = _INDEX_HTML.format(users='\n'.join(users_html))
    return index_html


def run_webserver(address, data_dir):
    global data_path
    data_path = data_dir
    website.run(*address)


def main(argv):
    if len(argv) != 3:
        print(f'USAGE: {argv[0]} <address> <data_dir>')
        return 1
    try:
        ip, port = argv[1].split(":")[0], int(argv[1].split(":")[1])
        path = argv[2]
        run_webserver((ip, port), path)
    except Exception as error:
        print(f'ERROR: {error}')
        return 1


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
