from modules.config.dbConfig import initiatePSqlSession
from flask import jsonify

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.userName = username
        self.password = password

    @classmethod
    def findUserCredentials(self, username):
        sqlSession = initiatePSqlSession()
        cursor = sqlSession.cursor()
        try:
            query = ("SELECT id,user_name,password FROM propel_users where user_name= %s")
            cursor.execute(query, (username,))
            row = cursor.fetchone()
            if row:
                user = User(row[0], row[1], row[2])
            else:
                user = None

            return user
        except Exception as e:
            print(e)
            cursor.close()
            return jsonify({'message': 'Error in Database connection'}), 401

        finally:
            cursor.close()
            if sqlSession is not None:
                sqlSession.close()
