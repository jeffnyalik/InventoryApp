from base64 import decode
from logging import exception
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from .models import CustomUser

def get_access_token(payload, expiry):
    token = jwt.encode(
        {"exp": datetime.now() + timedelta(days=expiry), **payload},
        settings.SECRET_KEY,
        algorithm="HS256"
    )

    return token



def decodeJWT(bearer):
    if not bearer:
        return None

    token = bearer[7:]
    try:
        decoded = jwt.decode(
            token, key=settings.SECRET_KEY, algorithms="HS256"
        )

    except Exception:
        return None

    if decoded:
        try:
            return CustomUser.objects.get(id=decoded["user_id"])
        except Exception:
            return None