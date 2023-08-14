import hashlib
import random
import uvicorn
from fastapi import FastAPI
from db.models import User

# app = FastAPI()
# app.include_router()


def generate_password():
    pass_len = 8
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''
    for i in range(pass_len):
        password += random.choice(chars)
    return password


def generate_passwords():
    users = User.get_users_with_no_hash()
    pass_json = {}
    for user in users:
        password = generate_password()
        pass_json[user.login] = password
        user.set_pwd(password)
        user.set_hash(hashlib.md5(password.encode()).hexdigest())
    return pass_json


if __name__ == '__main__':
    print(generate_passwords())
