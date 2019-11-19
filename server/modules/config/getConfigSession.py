import configparser
def getConfigSession(session):
    appConfig = configparser.RawConfigParser()
    appConfig.read("config.ini")
    sessionObj = appConfig[session]
    return sessionObj

