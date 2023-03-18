<<<<<<< HEAD
7-model_state_fetch_all.py
=======
#!/usr/bin/python3
"""
Script to list all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for id, name in session.query(State.id, State.name):
        print("{}: {}".format(id, name))

    session.close
>>>>>>> 8db4a942f6188b86fa6a63a117697dd2a1003f02
