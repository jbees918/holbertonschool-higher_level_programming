<<<<<<< HEAD
model_state.py
=======
#!/usr/bin/python3
"""
This python file contains the class definition of a State
and an instance Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
>>>>>>> 8db4a942f6188b86fa6a63a117697dd2a1003f02
