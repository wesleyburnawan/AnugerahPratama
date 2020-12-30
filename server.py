from flask import Flask
from flask import request
from flask import jsonify
from . import db
app = Flask(__name__)

@app.route('/users', methods=['POST'])
def createUserRequest():
    try:
        data = request.get_json(force=True)
        resp = jsonify({})
        db.createUser(data['username'], data['password'])
    except:
        return resp, 409
    return resp, 200

