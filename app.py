import time
from flask import Flask, send_from_directory, request
from flask_cors import CORS
app = Flask(__name__, static_folder='frontend/build/', static_url_path='/')
CORS(app)

@app.route('/api/signin', methods=['GET', 'POST'])
def sign_in():
    data = request.json

    u = data.get('username')
    p = data.get('password')
    return {'success' : u == p }

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json

    u = data.get('username')
    p = data.get('password')
    n = data.get('number')

    return {'success': True}

@app.route('/api/list_inventory', methods=['GET', 'POST'])
def inventory_list():
    if request.method == 'POST':
        return {'success': False}
    return {'success': True, 'data': [{'name': 'strawberry'}, {'name': 'blueberry'}, {'name': 'pineapple'}]}

@app.route('/api/inventory/<username>', methods=['GET', 'POST'])
def inventory(username):

    if request.method == 'POST':
        return {'success': False}
    
    return {'success': True, 'data': [{'name': 'strawberry', 'price': 100}, {'name': 'blueberry', 'price': 50}]}

@app.route('/api/predictions/<username>', methods=['GET'])
def predictions(username):
    return {'success': True, 'data': [{'name': 'strawberry', 'prediction': -5.6, 'confidence': 0.76 }, {'name': 'blueberry', 'prediction': 1.2, 'confidence': 0.4 }]}
    
# serve react built project
@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')