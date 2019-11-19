# app init file
# application factory combining all modules
from flask import Flask
from .config.jwtConfig import setJwtConfigInApp
from .config.chatConfig import setChatConfigInApp
from .config import getConfigSession 
from .config import configModule
from .business import businessModule
from .chat import chatModule
from .dataAccess import dataAccessModule
from flask_cors import CORS

from flask_socketio import SocketIO

def createApp():
    app=Flask(__name__)
    securedApp= setChatConfigInApp(setJwtConfigInApp(app))
    securedApp.register_blueprint(configModule)
    securedApp.register_blueprint(businessModule)
    securedApp.register_blueprint(chatModule)
    securedApp.register_blueprint(dataAccessModule)
    CORS(securedApp)
    return securedApp