from flask import Blueprint

dataAccessModule = Blueprint('dataAccessModule', __name__)

from modules.dataAccess import sampleDll