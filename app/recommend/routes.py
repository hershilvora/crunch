from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib, ssl, email
from app.recommend import recommend_bp


@recommend_bp.route('/email')  # would take recommendation from users to add a movie that not currently in database
def recommendation():
    return render_template('recommend.html')


@recommend_bp.route('/recommend_check', methods=['POST', 'GET'])
def recommend_confirm():  # take form and send email to people
    if request.method == 'POST':
        result = request.form
        m_name = result['movie_name']
        receiver_email = "crunchmovietest@gmail.com"
        user = result['user']
        subject = "Movie Recommendation: %s" % (m_name)
        email = result['msg']

        sender_email = "crunchmovietest@gmail.com"
        message = MIMEMultipart()
        text = """\
        User: %s
        Movie name: %s

        Why should it be added:
        %s""" % (
        user, m_name, email)  # add other things if needed, such as country of origin or what studio make the movie/when
        message.attach(MIMEText(text, 'plain'))
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, 'crunchtest123')
            server.sendmail(sender_email, receiver_email, message.as_string())

    return render_template('confirmation.html')