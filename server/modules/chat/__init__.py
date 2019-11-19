from flask import Blueprint
chatModule = Blueprint('chatModule', __name__)
from modules.chat import chat

