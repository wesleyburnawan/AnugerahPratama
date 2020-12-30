from flask import Flask
from flask import request
from flask import jsonify
from . import db
app = Flask(__name__)

@app.route('/users/create', methods=['POST'])
def createUserRequest():
    try:
        data = request.get_json(force=True)
        resp = jsonify({})
        db.createUser(data['username'], data['password'])
    except:
        return resp, 409
    return resp, 200 #or 201

@app.route('/users/delete', methods=['POST'])
def deleteUserRequest():
    try:
        data = request.get_json(force=True)
        resp = jsonify({})
        db.deleteUser(data['username'])
    except:
        return resp,404
    return resp, 200

@app.route('/users/update', methods=['POST'])
def updateUserRequest():
    try:
        data = request.get_json(force=True)
        resp = jsonify({})
        db.updateUser(data['oldUsername'], data['newUsername'], data['newPassword'])
    except:
        return resp, 404
    return resp, 200

@app.route('/users/login', methods=['POST', 'GET'])
def loginRequest(): #need work
    try:
        data = request.get_json(force=True)
        resp = jsonify({})
        account = db.login(data['username'],data['password'])
    except:
        return resp, 404
    return resp, 200