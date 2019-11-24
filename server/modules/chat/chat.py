def chatSession(socketio):

    @socketio.on('connect')
    def test_connect():
        print('Client connected')

    def messageReceived(methods=['GET', 'POST']):
        print('message was received!!!')

    @socketio.on('new-message')
    def handle_my_custom_event(json, methods=['GET', 'POST']):
        print('received my event: ' + str(json))
        socketio.emit('response', json, callback=messageReceived)
