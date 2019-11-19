from flask import jsonify, request, Response
from flask_jwt_extended import jwt_required

from modules.business import businessModule as BM
from modules.dataAccess import sampleDll as SDll


@BM.route('/api/getDegrees', methods=['POST'])
@jwt_required
def getDegrees():
    try:
        state = request.json.get('state')
        return SDll.getDegrees(state)
    except Exception as e:
        print(e)
        return jsonify({'message': 'Error Occured'}), 500