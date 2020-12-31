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

@app.route('/users/<username>', methods=['DELETE']) 
def deleteUserRequest(username):
    try:
        data = request.get_json(force=True)
        resp = jsonify({})
        db.deleteUser(username)
    except:
        return resp, 409
    return resp, 200

@app.route('/users/<username>', methods=['PUT'])
def updateUserRequest(username):
    try:
        data = request.get_json(force=True)
        resp = jsonify({})
        db.updateUser(username, data['username'], data['password'])
    except:
        return resp, 409
    return resp, 200

@app.route('/login', methods=['GET'])
def loginRequest(): 
    try:
        data = request.get_json(force=True)
        resp = jsonify({})
        inputPassword = db.login(data['username'])
        if inputPassword[0] != data['password']:
            return resp, 401
    except:
        return resp, 409
    return resp, 200