import os
import smtplib

EMAIL_ADDRESS = os.environ.get('GMAIL_ID')
EMAIL_PASSWORD = os.environ.get('GMAIL_ID_PASSWORD')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Python generated mail practice'
    body = 'work harder!'

    message = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'messirahul987@gmail.com', message)