from modules.authentication import authenticationModule
from flask import Flask, request, jsonify
from flask_jwt_extended import (JWTManager, get_jwt_identity)
from modules.config.getConfigSession import getConfigSession


def setJwtConfigInApp(app):
    app.register_blueprint(authenticationModule)
    app.config['JWT_SECRET_KEY'] = getConfigSession('jwtConfig')['secretKey']
    app.config["PROPAGATE_EXCEPTIONS"] = True
    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def expired_token_callback():
        return jsonify({
            'description': 'The Token has expired',
            'error': 'token_expired'
        }), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({
            'description': 'The Token is invalid',
            'error': 'token_invalid'
        }), 401

    @jwt.revoked_token_loader
    def revoked_token_callback():
        return jsonify({
            'description': 'The Token is revoked',
            'error': 'token_revoked'
        }), 401

    return app
