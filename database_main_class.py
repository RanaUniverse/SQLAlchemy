
'''
# pip install sqlalchemy
This is the main module where i will defines the class
-Rana Universe 🍌🍌🍌
'''


from datetime import date, time, datetime

from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.orm import declarative_base




Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id_ = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    email = Column(String)
    date_of_birth = Column(Date)


    def __init__(
        self,
        name:str = None,
        age: int = None,
        gender: str = None,
        email: str = None,
        date_of_birth: date =None
    ):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.date_of_birth = date_of_birth


    def __repr__(self):
        return f"<Student(id={self.id_},name={self.name}, age={self.age}, gender={self.gender}, email={self.email}, dob={self.date_of_birth})>"


