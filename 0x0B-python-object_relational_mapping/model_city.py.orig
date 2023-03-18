<<<<<<< HEAD

=======
#!/usr/bin/python3
"""
Python file like model_state.py named model_city.py
that contains the class definition of a City.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    City class that inherits from Base
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'))
>>>>>>> 8db4a942f6188b86fa6a63a117697dd2a1003f02
