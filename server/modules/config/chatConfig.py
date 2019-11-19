from flask_socketio import SocketIO
from modules.config.getConfigSession import getConfigSession

def setChatConfigInApp(app):
    app.config['SECRET_KEY'] = getConfigSession('chatConfig')['secretKey']
    socketio = SocketIO(app)
    socketio.run(app, debug=True)
    return app