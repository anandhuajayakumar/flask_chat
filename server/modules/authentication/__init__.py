# Authentication Module Init

from flask import Blueprint
authenticationModule=Blueprint('authenticationModule',__name__)

# Authentication Modules Entry

from modules.authentication import authBll
from modules.authentication import authDll
