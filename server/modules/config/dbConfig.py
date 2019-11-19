from modules.config import configModule
import psycopg2
import configparser
from modules.config.getConfigSession import getConfigSession


def initiatePSqlSession():
    config = getConfigSession('psqlDbConfig')
    host = config["host"]
    user = config["user"]
    password = config["password"]
    port = config["port"]
    dbName = config["dbname"]
    return psycopg2.connect(host=host, database=dbName, user=user, password=password)