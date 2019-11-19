from modules.config.dbConfig import initiatePSqlSession
from flask import jsonify
from modules.models import degree as degreeModel


def getDegrees(state):
    try:
        sqlSession = initiatePSqlSession()
        cursor = sqlSession.cursor()
        query = """
                SELECT DISTINCT degree_level_id, degree_level FROM propel_degree_state_map
                WHERE state=%s
                ORDER BY degree_level
                """
        cursor.execute(query, (str(state),))
        result = []
        row = cursor.fetchone()
        while row:
            result.append(
                degreeModel(row[0], row[1]).serialize())
            row = cursor.fetchone()
        return jsonify(result)
    except Exception as e:
        print(e)
        return jsonify({'message': 'Database error occured'}), 500