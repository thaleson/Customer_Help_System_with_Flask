from flask_socketio import SocketIO, emit

socketio = SocketIO()

@socketio.on('send_notification')
def handle_send_notification(data):
    """
    Manipula o evento 'send_notification' do Socket.IO.

    Este manipulador de eventos é chamado quando um cliente envia um evento 'send_notification'.
    Ele extrai a mensagem dos dados recebidos e a emite para todos os clientes conectados.

    Parâmetros:
        data (dict): Um dicionário contendo os dados do evento, incluindo a mensagem.

    Observações:
        - A mensagem é transmitida para todos os clientes conectados usando o parâmetro `broadcast=True`.
    """
    message = data.get('message')
    # Emite a notificação para todos os clientes conectados
    emit('notification', {'message': message}, broadcast=True)
