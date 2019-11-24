from werkzeug.security import safe_str_cmp
from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import bcrypt
import datetime
from modules.authentication import authenticationModule as auth
from modules.authentication.authDll import User


@auth.route('/api/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email', None)
        incomingPassword = request.json.get('password', None)
        user = User.findUserCredentials(email)
        if user:
            if bcrypt.checkpw(incomingPassword.encode('utf-8'), user.password.encode('utf-8')):
                expires = datetime.timedelta(days=1)
                accessToken = create_access_token(
                    identity=user.id, fresh=True, expires_delta=expires)
                token = {'token': accessToken}
                return jsonify(token), 200
            else:
                return jsonify({'message': 'Invalid Credentials'}), 200

        else:
            return jsonify({'message': 'Invalid Credentials'}), 401
    except Exception as e:
        print(e)
        return jsonify({'message': 'Error in Database connection'}), 401


@auth.route('/api/verifyToken', methods=['GET'])
@jwt_required
def verifyToken():
    current_user = get_jwt_identity()
    return jsonify({
        "title": 'Success'
    })

@auth.route('/api/healthCheck', methods = ['GET'])
def healthCheck():
    return jsonify({
        "title": 'Success'
    })