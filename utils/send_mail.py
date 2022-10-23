from email.message import EmailMessage
import smtplib
import ssl
import os

class Email:
    def __init__(self, sender, receiver, smtp_password):
        self.sender, self.receiver, self.smtp_password = sender, receiver, smtp_password

    def _parse_mail(self, subject, body):
        email = EmailMessage()
        email["From"] = self.sender
        email["To"] = self.receiver
        email["Subject"] = subject
        email.set_content(body)
        return email


    def send_code(self, subject, body):
        email = self._parse_mail(subject, body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.sender, self.smtp_password)
            smtp.sendmail(self.sender, self.receiver, email.as_string())

new_mail = Email("hamzaplojovic9@gmail.com", "hamzaplojovic9@gmail.com", os.environ["SMTP_PASSWORD"])
new_mail.send_code("test", "test")
