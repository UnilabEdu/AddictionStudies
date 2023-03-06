
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
from addiction.config import Config, Constants
from threading import Thread

def send_email(subject, text, recipients):
    from addiction.extensions import mail
    message=Message(subject=subject, html=text, recipients=[recipients], sender='mariam')
    thread=Thread(target=mail.send(message))
    thread.start()


def create_key(payload):
    serializer=URLSafeTimedSerializer(Config.SECRET_KEY)
    key=serializer.dumps(payload, salt=Constants.SERIALIZER_SALT)
    return key

def confirm_key(key):
    serializer=URLSafeTimedSerializer(Config.SECRET_KEY)
    try:
        payload=serializer.loads(key, salt=Constants.SERIALIZER_SALT, max_age=600)
        return payload
    except:
        return False
        