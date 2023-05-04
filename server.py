import json
from flask import Flask, request, Response, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/only_response')
def only_response():
    response = jsonify({"response":"This is a dummy response"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/request_response', methods=['POST'])
def request_response(request=request):
    req_data = request.get_json()
    response = jsonify({"response":"This is a dummy response", "yourRequestData":req_data["request_data"]})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    #return Response(json.dumps({"response":query}), status=200, mimetype='application/json') 

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8787)






#
