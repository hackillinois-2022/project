
from flask import Flask, send_from_directory, request
from flask import Flask, request, Response
import json
from backend.config import config as cfg

from backend.service.service import Service
from flask_cors import CORS
app = Flask(__name__, static_folder='frontend/build/', static_url_path='/')
CORS(app)

service = Service()
@app.route('/api/signin', methods=['POST'])
def sign_in():
        try:
            request_data = request.get_data()
            response = Response()
            if not request_data:
                response.data = json.dumps({"message": "No input data to process", "success" : False})
                response.status_code = 200
                return response

            request_data = json.loads(request_data)
            output_data, response.status_code = service.get_user_data(**request_data)
            response.data = json.dumps(output_data, default=str)
            return response
        except Exception as e:
            print("Error while parsing data")
            print(e.args)
            response = Response(status=200)
            response.data = json.dumps({"message": "Error while parsing data","success" : False})
            return response

@app.route('/api/register', methods=['POST'])
def register():
    """
    Using HTTP POST method to insert an inventory record
    :return : Response_object: Success or failure message
    """
    try:
        request_data = request.get_data()
        response = Response()
        if not request_data:
            response.data = json.dumps({"message": "No input data to process", "success" : False})
            response.status_code = 200
            return response
        request_data = json.loads(request_data)
        output_data, response.status_code = service.add_user_data(**request_data)
        response.data = json.dumps(output_data, default=str)
        return response
    except Exception as e:
        print("Error while parsing data")
        print(e.args)
        response = Response(status=200)
        response.data = json.dumps({"message": "Error while parsing data", "success" : False})
        return response

@app.route('/api/inventory', methods=['POST'])
def inventory():
    """
    Using HTTP POST method to insert an inventory record
    :return : Response_object: Success or failure message
    """

    try:
        request_data = request.get_data()
        response = Response()
        if not request_data:
            response.data = json.dumps({"message": "No input data to process", "success" : False})
            response.status_code = 200
            return response
        request_data = json.loads(request_data)
        output_data, response.status_code = service.add_produce(**request_data)
        response.data = json.dumps(output_data, default=str)
        return response
    except Exception as e:
        print("Error while parsing data")
        print(e.args)
        response = Response(status=200)
        response.data = json.dumps({"message": "Error while parsing data", "success" : False})
        return response

@app.route('/api/inventory', methods=['GET'])
def inventory_get():
    """
    Using HTTP POST method to insert an inventory record
    :return : Response_object: Success or failure message
    """
    try:
        request_data = request.args.get("username")
        response = Response()
        if not request_data:
            response.data = json.dumps({"message": "No input data to process", "success": False})
            response.status_code = 200
            return response
        output_data, response.status_code = service.get_produce(request_data)
        response.data = json.dumps(output_data, default=str)
        return response
    except Exception as e:
        print("Error while parsing data")
        print(e.args)
        response = Response(status=200)
        response.data = json.dumps({"message": "Error while parsing data", "success": False})
        return response

@app.route('/api/inventory', methods=['DELETE'])
def inventory_delete():
    """
    Using HTTP POST method to insert an inventory record
    :return : Response_object: Success or failure message
    """
    try:
        request_data = request.get_data()
        response = Response()
        if not request_data:
            response.data = json.dumps({"message": "No input data to process", "success": False})
            response.status_code = 200
            return response
        request_data = json.loads(request_data)
        output_data, response.status_code = service.delete_produce(**request_data)
        response.data = json.dumps(output_data, default=str)
        return response
    except Exception as e:
        print("Error while parsing data")
        print(e.args)
        response = Response(status=200)
        response.data = json.dumps({"message": "Error while parsing data", "success": False})
        return response

@app.route('/api/predictions', methods=['GET'])
def predictions():
    try:
        request_data = request.args.get("username")
        response = Response()
        if not request_data:
            response.data = json.dumps({"message": "No input data to process", "success": False})
            response.status_code = 200
            return response
        output_data, response.status_code = service.make_prediction(request_data)
        response.data = json.dumps(output_data, default=str)
        return response
    except Exception as e:
        print("Error while parsing data")
        print(e.args)
        response = Response(status=200)
        response.data = json.dumps({"message": "Error while parsing data", "success": False})
        return response

@app.route('/api/predictions/plot', methods=['GET'])
def predictions_plot():
    try:
        request_data = request.args.get("username")
        response = Response()
        if not request_data:
            response.data = json.dumps({"message": "No input data to process", "success": False})
            response.status_code = 200
            return response
        output_data, response.status_code = service.prediction_plot(request_data)
        response.data = json.dumps(output_data, default=str)
        return response
    except Exception as e:
        print("Error while parsing data")
        print(e.args)
        response = Response(status=200)
        response.data = json.dumps({"message": "Error while parsing data", "success": False})
        return response
#
# serve react built project
@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(host=cfg.application_host, debug=True, port=cfg.application_port)