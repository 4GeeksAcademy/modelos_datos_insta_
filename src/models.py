from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    nickname: Mapped[str] = mapped_column(String(10))
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    content: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    like: Mapped[int]= mapped_column(Integer)
    url: Mapped[str] = mapped_column(String)


class Coment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'))
    content: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    like: Mapped[int]= mapped_column(Integer)

class Followers(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    follower_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    followed_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    date: Mapped[int]= mapped_column(Integer)


    


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
