
from flask import Flask, send_from_directory, request
from flask import Flask, request, Response
import json
from backend.config import config as cfg

from backend.service.service import Service
from flask_cors import CORS
app = Flask(__name__, static_folder='frontend/build/', static_url_path='/')
CORS(app)

service = Service()
@app.route('/api/signin', methods=['GET', 'POST'])
def sign_in():
        print("I'm here")
        try:
            request_data = request.get_data()
            response = Response()
            if not request_data:
                response.data = json.dumps({"message": "No input data to process"})
                response.status_code = 400
                return response

            request_data = json.loads(request_data)
            output_data, response.status_code = service.get_user_data(**request_data)
            response.data = json.dumps(output_data, default=str)
            return response
        except Exception as e:
            print("Error while parsing data")
            print(e.args)
            response = Response(status=400)
            response.data = json.dumps({"message": "Error while parsing data"})
            return response

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
    app.run(host=cfg.application_host, debug=True, port=cfg.application_port)