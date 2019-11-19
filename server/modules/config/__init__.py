# Config init file

from flask import Blueprint
configModule=Blueprint('configModule',__name__)

# Config Modules Entry

from modules.config import dbConfig
from modules.config import jwtConfig
from modules.config import chatConfig