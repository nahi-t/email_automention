import smtplib
from email.mime.text import MIMEText

def sendEmail():
    sender = "@gmail.com"
    receiver = "someone@example.com"
    password = "your-app-password-here"  

    msg = MIMEText("Hello, this is a test email.")
    msg["Subject"] = "Test Email"
    msg["From"] = sender
    msg["To"] = receiver

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()

sendEmail()
