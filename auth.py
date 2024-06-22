from database import *
import hashlib

def register_user(user):
    hashed_password = hashlib.sha256(user['password'].encode('utf-8')).hexdigest()
    user['password'] = hashed_password
    return create_user(user)

def authenticate_user(username, password):
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return verify_user_credentials(username, hashed_password)

def get_user_role(user_id):
    return read_user_role(user_id)