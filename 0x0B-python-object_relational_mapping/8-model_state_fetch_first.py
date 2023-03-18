<<<<<<< HEAD
8-model_state_fetch_first.py
=======
#!/usr/bin/python3
"""
Script to print the first State object from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    if first := session.query(State).order_by(State.id).first():
        print(f"{first.id}: {first.name}")
    else:
        print("Nothing")

    session.close()
>>>>>>> 8db4a942f6188b86fa6a63a117697dd2a1003f02
