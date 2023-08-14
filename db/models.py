from sqlalchemy import Column, Integer, String, select
from config import Base, session


class User(Base):
    __tablename__ = 'USERS'
    id = Column(Integer, primary_key=True)
    pwd_hash = Column(String)
    login = Column(String)
    name = Column(String)
    access_level = Column(Integer)
    pwd = Column(String)

    @classmethod
    def get_users_with_no_hash(cls):
        return session.scalars(select(cls).where(cls.pwd_hash.is_(None))).all()

    def set_hash(self, hash: str):
        self.pwd_hash = hash
        session.commit()

    def set_pwd(self, pwd: str):
        self.pwd = pwd
        session.commit()

    @classmethod
    def add_user(cls, login: str):
        user = cls(login=login, name='test', access_level=1, pwd='test')
        session.add(user)
        session.commit()
