#from Sorteador import part
import smtplib
from email.message import EmailMessage

def main(email, link):
    msg = EmailMessage()
    msg.set_content(f'''Encontramos um desconto para seu produto!!
    Confira mais aqui: {link}
    ''')
    msg['Subject'] = 'Seu desconto chegou'
    msg['From'] = 'email@email.com'
    msg['To'] = email
    smtp = "smtp.gmail.com"
    server = smtplib.SMTP(smtp, 587)
    server.starttls()
    server.login(msg['From'], 'senhadoemail')
    server.send_message(msg)
    server.quit()
