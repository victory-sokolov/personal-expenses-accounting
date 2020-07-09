from flask_mail import Message
from flask import render_template
from project import create_app
from flask_mail import Mail

app = create_app('development')
mail = Mail(app)

def send_email(to, subject, template, **kwargs):
    msg = Message(
        subject,
        recipients=[to],
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
