import hashlib
import random

from sqlalchemy import Column, Integer, String, select
from src.config import Base, session


class User(Base):
    __tablename__ = 'USERS'
    id = Column(Integer, primary_key=True)
    pwd_hash = Column(String)
    login = Column(String)
    name = Column(String)
    access_level = Column(Integer)
    pwd = Column(String)
    stock = Column(String)
    stock_role_id = Column(Integer)

    @classmethod
    def get_users_with_no_hash(cls):
        return session.scalars(select(cls).where(cls.pwd_hash.is_(None)).order_by(cls.stock, cls.stock_role_id)).all()

    @classmethod
    def add_user(cls, login: str):
        user = cls(login=login, name='test', access_level=1, pwd='test')
        session.add(user)
        session.commit()

    @staticmethod
    def _generate_password():
        pass_len = 8
        chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        password = ''
        for i in range(pass_len):
            password += random.choice(chars)
        return password

    def generate_passwords(self):
        pass_json = {}
        for user in self.get_users_with_no_hash():
            password = self._generate_password()
            pass_json[user.login] = password
            user.pwd = password
            user.pwd_hash = hashlib.md5(password.encode()).hexdigest()
        return pass_json
