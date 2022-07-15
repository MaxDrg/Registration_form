import ssl
import smtplib
from django.conf import settings
from email.message import EmailMessage

class Email:
    def __init__(self, receiver: str) -> None:

        self.__email_sender = settings.EMAIL_SENDER
        self.__email_password = settings.EMAIL_PASSWORD
        self.__email_provider = settings.EMAIL_PROVIDER
        
        self.email_receiver = receiver
        self.subject = 'Registration for the Conference'

    def send_email(self, body: str):
        em = EmailMessage()
        em['From'] = self.__email_sender
        em['To'] = self.email_receiver
        em['Subject'] = self.subject
        em.set_content(body)

        with smtplib.SMTP_SSL(self.__email_provider, 465, context=ssl.create_default_context()) as smtp:
            smtp.login(self.__email_sender, self.__email_password)
            smtp.sendmail(self.__email_sender, self.email_receiver, em.as_string())