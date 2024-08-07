document.getElementById('notificationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const clientInput = document.getElementById('client');
    const messageInput = document.getElementById('message');
    const client = clientInput.value;
    const message = messageInput.value;
    
    // Enviar a notificação para o servidor
    fetch('/send_notification', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ client: client, message: message })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'Notification sent!') {
            alert('Solicitação de ajuda enviada com sucesso!');
            if (data.redirect) {
                window.location.href = data.redirect;
            }
        }
    });
    
    // Limpar os campos de entrada
    clientInput.value = '';
    messageInput.value = '';
});
