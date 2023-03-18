<<<<<<< HEAD
12-model_state_update_id_2.py
=======
#!/usr/bin/python3
"""
Script changes the name of a State
object from the database hbtn_0e_6_usa
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

    item = session.query(State).filter_by(id='2').first()
    item.name = "New Mexico"
    session.commit()

    session.close()
>>>>>>> 8db4a942f6188b86fa6a63a117697dd2a1003f02
