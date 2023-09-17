#!/usr/bin/python3
""" Fetch ALl states"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    del_rows = State.delete().where(State.name.like('%a%'))
    if del_row:
        session.execute(del_rows)
        session.commit()
    session.close()
