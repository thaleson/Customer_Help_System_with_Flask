# 🛠️ Sistema de Notificações e Ajuda ao Cliente

Bem-vindo ao sistema de notificações e ajuda ao cliente! 🎉 Este projeto foi desenvolvido utilizando Flask e Socket.IO para fornecer um sistema de envio e exibição de notificações, bem como um fluxo de ajuda ao cliente. 🚀

## 📜 Funcionalidades

- **Página Inicial**: Acesso ao sistema com redirecionamento para a página de ajuda. 🏠
- **Solicitação de Ajuda**: Envio de solicitações de ajuda que são exibidas em tempo real. 📩
- **Exibição de Notificações**: Visualização das notificações enviadas. 📜

## 🚀 Instruções para Iniciar o Projeto

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/thaleson/Customer_Help_System_with_Flask
   ```

2. **Instale as Dependências**:

   Primeiro, crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

   Em seguida, instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as Variáveis de Ambiente**:

   Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

   ```env
   SECRET_KEY=seu_segredo_aqui
   CORS_ALLOWED_ORIGINS=http://127.0.0.1:5500
   ```

4. **Inicie o Servidor**:

   Execute o seguinte comando para iniciar o servidor:

   ```bash
   python run.py
   ```

   O servidor estará disponível em `http://localhost:5000`. 🌐

## 💻 Estrutura do Projeto

- **app/**: Contém a lógica do aplicativo Flask.
  - **`__init__.py`**: Configuração e inicialização do Flask e Socket.IO.
  - **config.py**: Configurações de ambiente.
  - **routes.py**: Rotas e lógica do Flask.
  - **services.py**: Funções de serviço para notificações.
  - **socketio_instance.py**: Configuração do Socket.IO.
- **templates/**: Contém os arquivos HTML.
- **static/**: Contém os arquivos CSS e JS.
- **.env**: Arquivo de variáveis de ambiente.
- **run.py**: Script para iniciar o servidor.

## 🧩 Exemplos de Uso

### Enviar Notificação

Preencha o formulário na página inicial e envie uma notificação. 📝

### Exibir Notificações

Após enviar uma notificação, você será redirecionado para a página de notificações onde poderá ver todas as notificações enviadas. 👀

## 🛠️ Tecnologias Utilizadas

- **Flask**: Framework para desenvolvimento web.
- **Socket.IO**: Biblioteca para comunicação em tempo real.
- **eventlet**: Para suporte a WebSocket.

## 🤝 Contribuindo

Sinta-se à vontade para contribuir com melhorias! Para sugestões e correções, abra uma issue ou envie um pull request. 💪

## 📄 Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes. 📝




