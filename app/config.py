from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    """
    Classe base para configurações do Flask.

    Atributos:
        SECRET_KEY (str): Chave secreta usada para criptografia e segurança. 
                          A chave é carregada das variáveis de ambiente e tem um valor padrão se não estiver definida.
        CORS_ALLOWED_ORIGINS (list): Lista de URLs permitidas para CORS. 
                                      Carregada das variáveis de ambiente e dividida por vírgulas.
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')  # Use 'default_secret_key' se a variável não estiver definida
    CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', '').split(',')

class DevelopmentConfig(Config):
    """
    Configurações específicas para o ambiente de desenvolvimento.

    Atributos:
        DEBUG (bool): Ativa o modo de depuração, fornecendo mais informações sobre erros.
    """
    DEBUG = True
    # Outras configurações específicas de desenvolvimento

class TestingConfig(Config):
    """
    Configurações específicas para o ambiente de teste.

    Atributos:
        TESTING (bool): Ativa o modo de teste, que permite testes com o Flask.
    """
    TESTING = True
    # Outras configurações específicas de teste

class ProductionConfig(Config):
    """
    Configurações específicas para o ambiente de produção.

    Atributos:
        Não são especificados atributos adicionais nesta classe. 
        Pode-se adicionar configurações específicas para a produção, como configurações de log, cache, etc.
    """
    # Configurações específicas de produção
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
