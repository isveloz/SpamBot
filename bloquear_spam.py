    import smtplib
from email.mime.text import MIMEText

def bloquear_spam(username, password, sender_emails):
    # Establecer conexión con el servidor SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)

    # Obtener los correos electrónicos no deseados
    server.select('inbox')

    # Marcar los correos electrónicos como spam
    for sender_email in sender_emails:
        _, data = server.search(None, f'FROM "{sender_email}"')
        email_ids = data[0].split()

        for email_id in email_ids:
            server.store(email_id, '+X-GM-LABELS', '\\Spam')
            print(f"Se ha bloqueado el correo con ID: {email_id}")

    # Cerrar la conexión con el servidor SMTP
    server.logout()

# Configurar los datos de acceso a tu cuenta de correo
username = 'isaiasveloz41@gmail.com'
password = 'isaias.veloz_'

# Configurar los remitentes de spam que deseas bloquear
sender_emails = [
    'no-reply@twitch.tv',
    'reminders@facebookmail.com',
    'contacto@mail.lider.cl',
    'Pixabay@community.pixabay.com',
    'careers@marriotthiring.com',
    'cuesupport@avid.games',
    'rcumana@trabajando.com',
    'katerinasmn649@gmail.com',
    'recomendaciones@computrabajo.com',
    'no-reply@n.dribbble.com',
    'friendsuggestion@facebookmail.com'
    'noreply@redditmail.com'
]

# Bloquear el spam
bloquear_spam(username, password, sender_emails)
