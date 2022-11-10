import ssl
import smtplib
from email_confirmation import code
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:

    def __init__(self, sender, receiver, smtp_password):
        self.sender, self.receiver, self.smtp_password = sender, receiver, smtp_password

    def _parse_mail(self) -> MIMEMultipart:
        email = MIMEMultipart('alternative')
        email["From"] = self.sender
        email["To"] = self.receiver
        email["Subject"] = "Confirm your email address"
        html_part = MIMEText(code, 'html')
        email.attach(html_part)
        return email

    def send_code(self) -> str:
        email = self._parse_mail()
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.sender, self.smtp_password)
            smtp.sendmail(self.sender, self.receiver, email.as_string())

        return f"Code sent to {self.receiver}"
