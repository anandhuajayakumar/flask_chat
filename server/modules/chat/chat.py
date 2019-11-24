def chatSession(socketio):

    @socketio.on('connect', namespace='/test')
    def test_connect():
        print('Client connected')

    def messageReceived(methods=['GET', 'POST']):
        print('message was received!!!')

    @socketio.on('new-message')
    def handle_my_custom_event(json, methods=['GET', 'POST']):
        print('received my event: ' + str(json))
        socketio.emit('my response', json, callback=messageReceived)
