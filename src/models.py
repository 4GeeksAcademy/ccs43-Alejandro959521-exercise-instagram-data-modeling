import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False,unique=True)  
    firstname = Column(String(50),nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50),nullable=False,unique=True)   
    post= relationship("Post",back_populates="user")
    follower=relationship( "Follower",back_populates="user")

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id=Column(ForeignKey('user.id'))
    user_to_id=Column(ForeignKey('user.id'))
    user=relationship("User",back_populates="follower")
    
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.

class Media(Base):
    __tablename__ = 'media'
    id=Column(Integer, primary_key=True)
    type =Column(String(50), nullable=False)
    url=Column(String(250), nullable=False)
    post_id=Column(ForeignKey('post.id'))
    post=relationship("Post",back_populates="media")
   
class Post(Base):
    __tablename__ ='post'
    id=Column(Integer,primary_key=True)
    user_id=Column(ForeignKey('user.id'))
    user=relationship("User",back_populates="post")
    media=relationship("Media",back_populates="post")
    comment=relationship("Comment",back_populates="post")

class Comment(Base):
    __tablename__ ='comment'   
    id=Column(Integer,primary_key=True)
    comment_text=Column(String(250), nullable=False)
    author_id=Column(ForeignKey('user.id'))
    usuario=relationship("User",back_populates="comment")
    post_id=Column(ForeignKey('post.id'))
    post=relationship("Post",back_populates="comment")

   # def to_dict(self):
    #    return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
