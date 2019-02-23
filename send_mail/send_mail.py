#!/usr/bin/python

# Python mail script with smtplib, email.utils and email.mime.text.

# --- imports ---
import base64
import os
import smtplib
import email.utils
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.nonmultipart import MIMENonMultipart
from email.mime.text import MIMEText

# --- create our message ---

# Create our message.
message = """From: Ariel <do-not-replay@ariel.ac.il>
To: meve <meve@getnada.com>
Subject: Test

This is a test e-mail message.
"""
msg = MIMEText(message)
sender = 'do-not-replay@ariel.ac.il'
receivers = ['meve@getnada.com']

message = MIMEMultipart()
message['To'] = email.utils.formataddr(('meve', 'meve@getnada.com'))
message['From'] = email.utils.formataddr(('Ariel', 'do_not_replay@ariel.ac.il'))
message['Subject'] = 'Test'
message.attach(msg)

# --- add an attachment ---
file_name = "test_result.pdf"

part = MIMEBase('application', "octet-stream")
part.set_payload(open(os.path.join(os.path.dirname(__file__), file_name), 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(file_name))
message.attach(part)

# --- send the email ---
try:
    # SMTP() is used with normal, unencrypted (non-SSL) email.
    # To send email via an SSL connection, use SMTP_SSL().
    server = smtplib.SMTP()

    # Specifying an empty server.connect() statement defaults to ('localhost', 25).
    # Therefore, we specify which mail server we wish to connect to.
    server.connect('127.0.0.1')

    # Optional login for the receiving mail_server.
    # server.login ('login@example.com', 'Password')

    # Dump communication with the receiving server straight to to the console.
    server.set_debuglevel(True)

    # 'yourname@yourdomain.com' is our envelope address and specifies the return
    # path for bounced emails.
    server.sendmail(sender, receivers, message.as_string())
    print("Successfully sent email!")
except smtplib.SMTPException:
    print("Error: unable to send email")
finally:
    server.quit()
