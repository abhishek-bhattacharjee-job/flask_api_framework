
import json
from flask import Flask, request, Response, render_template, send_from_directory, jsonify
from flask_cors import CORS
app = Flask(__name__, static_url_path='', static_folder='frontend')
CORS(app)

from transformers import AutoModelWithLMHead, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("./models/tokenizer/")
model = AutoModelWithLMHead.from_pretrained("./models/model/")
def get_sql(raw_text):
    input_text = "translate English to SQL: %s </s>" % raw_text
    features = tokenizer([input_text], return_tensors='pt')
    output = model.generate(input_ids=features['input_ids'], attention_mask=features['attention_mask'])
    pred = tokenizer.decode(output[0])
    pred = pred.replace("<pad> ", "")
    query = pred.replace("</s>", "")
    return query

@app.route('/')
def home():
   return app.send_static_file('1.html')

@app.route('/predictSQLQuery', methods=['POST'])
def saveTextFile(request=request):
    req_data = request.get_json()
    print(req_data["raw_text"])
    query = get_sql(req_data["raw_text"])
    response = jsonify({"response":query})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    #return Response(json.dumps({"response":query}), status=200, mimetype='application/json')

if __name__ == '__main__':
   app.run(host="0.0.0.0", port="3001")






#
