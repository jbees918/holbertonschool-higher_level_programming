<<<<<<< HEAD
14-model_city_fetch_by_state.py
=======
#!/usr/bin/python3
"""
Script 14-model_city_fetch_by_state.py prints
all City objects from the database hbtn_0e_14_usa:
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    item = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()

    for city, state in item:
        print(f'{state.name}: ({city.id}) {city.name}')

    session.close()
>>>>>>> 8db4a942f6188b86fa6a63a117697dd2a1003f02
