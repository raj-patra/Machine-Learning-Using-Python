import os
import smtplib
from email.message import EmailMessage
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = "YOUR_PWD_HERE"
#contacts = ['bachisidhu26@gmail.com', 'bachisidhu62@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'bachittarjeet@gmail.com'

msg.set_content('This is a plain text email')
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)



