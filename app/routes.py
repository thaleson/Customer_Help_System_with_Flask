from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from .services import send_notification, get_notifications

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/send_notification', methods=['POST'])
def send_notification_route():
    data = request.json
    client = data.get('client')
    message = data.get('message')
    
    # Envia a notificação e adiciona à lista
    send_notification(client, message)
    
    # Envia uma resposta indicando sucesso e o URL para redirecionamento
    return jsonify({'status': 'Notification sent!', 'redirect': url_for('routes.notifications_page')})

@routes.route('/notifications')
def notifications_page():
    # Obtemos a lista de notificações e renderizamos a página
    notifications = get_notifications()
    return render_template('notificacao_sucess.html', notifications=notifications)

def init_app(app):
    app.register_blueprint(routes)
