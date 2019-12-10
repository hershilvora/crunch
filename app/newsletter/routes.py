from flask import render_template, request
from email.mime.text import MIMEText
import smtplib, ssl
from app.newsletter import newsletter_bp
from app.api import users

@newsletter_bp.route('/email')
def email():
    return render_template('email.html')


@newsletter_bp.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form

        receiver_email = users.get_subscribers()


        subject = result['subject']
        email = result['email']

        for x in receiver_email:
            sender_email = "crunchmovietest@gmail.com"

            text = """%s""" %(email)

            message = MIMEText(text)
            message["Subject"] = subject
            message["From"] = sender_email
            message["To"] = x

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, 'crunch123')
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )

        return render_template('email_result.html')