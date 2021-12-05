import bcrypt
import os
from configs.config import ADMIN_ACCESS_LEVEL
from datetime import datetime
from uuid import uuid4


def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode(), hashed_password)


def get_password_hash(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_user_admin(current_user):
    if current_user.access_level == ADMIN_ACCESS_LEVEL:
        return current_user
    else:
        return False


def date_to_iso_date(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f%z')
    except:
        date = datetime.strptime(
            f"{date}T12:00:30.575+00:00", '%Y-%m-%dT%H:%M:%S.%f%z')
    return date


def handle_id_for_model(data):
    if data:
        id = data.get("_id", None)
        if id:
            data["_id"] = str(data["_id"])
        return data


def create_dir(dir):
    try:
        if not os.path.isdir(dir):
            os.makedirs(dir)
        return True
    except Exception as err:
        return False


def delete_file(file):
    try:
        if os.path.isfile(file):
            os.remove(file)
            return True
        else:
            return False
    except Exception as err:
        return False


def generate_unique_id():
    unique_id = uuid4()
    return str(unique_id)
