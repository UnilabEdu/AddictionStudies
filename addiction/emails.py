from flask_mail import Message
from flask import g, copy_current_request_context
from itsdangerous import URLSafeTimedSerializer
from threading import Thread

from addiction.config import Config, Constants
from addiction.extensions import mail


def send_email(subject, text, recipients):
    message = Message(subject=subject, html=text, recipients=[recipients], sender='mariam')

    @copy_current_request_context
    def send_message(message):
        mail.send(message)

    thread = Thread(target=send_message, args=[message])
    thread.start()


def create_key(payload):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    key = serializer.dumps(payload, salt=Constants.SERIALIZER_SALT)
    return key


def confirm_key(key):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    try:
        payload = serializer.loads(key, salt=Constants.SERIALIZER_SALT, max_age=600)
        return payload
    except:
        return False
