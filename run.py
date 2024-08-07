import eventlet
eventlet.monkey_patch()  # Isto deve ser chamado antes de importar qualquer outro módulo

from app import create_app
from app.socketio_instance import socketio

# Cria a instância da aplicação Flask com a configuração 'development'
app = create_app('development')

if __name__ == '__main__':
    """
    Executa a aplicação Flask com suporte a Socket.IO usando o Eventlet.

    - `eventlet.monkey_patch()`: Modifica o comportamento padrão de alguns módulos da biblioteca padrão do Python
      para fornecer suporte a operações assíncronas, que são necessárias para o funcionamento adequado do Socket.IO.
    - `create_app('development')`: Cria a aplicação Flask com a configuração de desenvolvimento.
    - `socketio.run()`: Inicia o servidor Socket.IO com a aplicação Flask.
      - `host='0.0.0.0'`: Faz com que o servidor escute em todas as interfaces de rede disponíveis.
      - `port=5000`: Define a porta em que o servidor irá escutar.
      - `debug=True`: Ativa o modo de depuração para ajudar no desenvolvimento.
    """
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
