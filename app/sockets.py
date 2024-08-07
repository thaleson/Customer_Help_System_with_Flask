from .socketio_instance import socketio

def init_socketio():
    """
    Inicializa os manipuladores de eventos do Socket.IO.

    Este método configura os manipuladores de eventos para quando um cliente se conecta ou desconecta.
    - O evento 'connect' é acionado quando um cliente estabelece uma conexão com o servidor.
    - O evento 'disconnect' é acionado quando um cliente encerra a conexão com o servidor.
    """

    @socketio.on('connect')
    def handle_connect():
        """
        Manipula o evento de conexão do Socket.IO.

        Este manipulador de eventos é chamado quando um cliente se conecta ao servidor.
        A mensagem 'Client connected' é impressa no console para indicar a nova conexão.
        """
        print('Client connected')

    @socketio.on('disconnect')
    def handle_disconnect():
        """
        Manipula o evento de desconexão do Socket.IO.

        Este manipulador de eventos é chamado quando um cliente se desconecta do servidor.
        A mensagem 'Client disconnected' é impressa no console para indicar a desconexão.
        """
        print('Client disconnected')
