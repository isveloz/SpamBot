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
username = ''
password = ''

# Configurar los remitentes de spam que deseas bloquear
sender_emails = [
]

# Bloquear el spam
bloquear_spam(username, password, sender_emails)
