from flask import Flask
from flask_cors import CORS
from .config import config
from .socketio_instance import socketio

cors = CORS()

def create_app(config_name='default'):
    """
    Cria e configura uma instância da aplicação Flask.

    Parâmetros:
        config_name (str): Nome do ambiente de configuração a ser carregado. 
                           O valor padrão é 'default'.

    Retorna:
        Flask: A instância configurada da aplicação Flask.

    Configurações:
        - Carrega a configuração apropriada com base em `config_name`.
        - Inicializa o CORS com as origens permitidas definidas na configuração.
        - Configura o Socket.IO com as origens permitidas para CORS.
        - Registra as rotas e sockets para a aplicação.
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    cors.init_app(app)
    socketio.init_app(app, cors_allowed_origins=config[config_name].CORS_ALLOWED_ORIGINS)

    from . import routes
    routes.init_app(app)

    from . import sockets
    sockets.init_socketio()

    return app
