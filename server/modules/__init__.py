# app init file
# application factory combining all modules
from flask import Flask
from .config.jwtConfig import setJwtConfigInApp
from .config.chatConfig import setChatConfigInApp
from .config import getConfigSession 
from .config import configModule
from .business import businessModule
from .chat import chatModule
from .chat.chat import chatSession
from .dataAccess import dataAccessModule
from flask_cors import CORS

from flask_socketio import SocketIO

def createApp():
    app=Flask(__name__)
    securedApp= setJwtConfigInApp(app)
    securedApp.register_blueprint(configModule)
    securedApp.register_blueprint(businessModule)
    securedApp.register_blueprint(chatModule)
    securedApp.register_blueprint(dataAccessModule)
    CORS(securedApp)

    (socketio, app) = setChatConfigInApp(securedApp)

    chatSession(socketio)

    return (socketio, app)