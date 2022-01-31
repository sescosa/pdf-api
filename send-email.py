import smtplib
import email
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from secrets import sender_email, receiver_email, password

"""
https://fedingo.com/how-to-send-html-mail-with-attachment-using-python/
"""

msg = MIMEMultipart("alternative")
msg["Subject"] = "Pago Curso Econometría - Pam Learning"
msg["From"] = sender_email
msg["To"] = receiver_email
filename = "invoice0.pdf"

views = "235"

html = f"""\
<html>
  <body>
    <p><b>Adjunto tienes el recibo del pago de las ventas de tu curso desde Julio 2021.</b><br>
       Esto es un test.<br>
       Tus videos se han visto durante un total de {views} minutos.<br>
    </p>
    <p>Equipo Pam Learning</p>
  </body>
</html>
"""

part = MIMEText(html, "html")
msg.attach(part)

with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    "attachment", filename= filename
)
msg.attach(part)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, msg.as_string()
    )