from flask import Flask, request, jsonify
from utils.tools import AppTools 

# initialize flask app
app = Flask(__name__)
# initialize AppTools
tools = AppTools()

# 1- route pour crypter une text
@app.route("/crypt", methods=['POST'])
def crypt():
    # reception de text a crypter
    data = request.get_json()
    text = data.get('text')
    return jsonify({"new_text": tools.crypt(text), 'key': tools.key})

# 2- route pour decrypter une text
@app.route("/decrypt", methods=['POST'])
def decrypt():
    # recuperation de text a decrypter et sa cle
    data = request.get_json()
    text = data.get("text")
    key = data.get("key")
    
    return jsonify({"text": tools.decrypt(text, key)})

# 3- route pour hasher une texte
@app.route('/hash', methods=['POST'])
def hash():
    # recuperation de text
    data = request.get_json()
    text = data.get('text')
    return jsonify({"new_text": tools.hash(text)})

# 4- route pour comparer deux hash
@app.route('/compare', methods=['POST'])
def compare():
    # recuperation de text et hash
    data = request.get_json()
    text = data.get('text')
    hash_to_compare = data.get('hash')
    
    is_match = tools.compare_hash(text, hash_to_compare)
    return jsonify({"match": is_match, "message": "Les hash correspondent" if is_match else "Les hash ne correspondent pas"})

# cors configuration
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# run server
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)