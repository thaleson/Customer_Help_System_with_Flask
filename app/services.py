# services.py

notifications = []

def send_notification(client, message):
    """
    Adiciona uma notificação à lista de notificações e a emite via Socket.IO.

    Parâmetros:
        client (str): O identificador ou nome do cliente que enviou a notificação.
        message (str): A mensagem da notificação.

    Observações:
        - A notificação é armazenada na lista `notifications`.
        - Se estiver configurado o Socket.IO, a notificação é emitida para todos os clientes conectados.
    """
    # Adicione a mensagem à lista de notificações associadas ao cliente
    notifications.append({'client': client, 'message': message})
    
    # Em caso de uso com Socket.IO, a mensagem seria emitida aqui também
    from .socketio_instance import socketio
    socketio.emit('notification', {'client': client, 'message': message})

def get_notifications():
    """
    Retorna a lista de todas as notificações.

    Retorna:
        list: Uma lista de dicionários, onde cada dicionário contém informações sobre o cliente e a mensagem da notificação.
    """
    return notifications
