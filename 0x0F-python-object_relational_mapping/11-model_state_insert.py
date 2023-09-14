#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select, insert

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    with engine.connect() as connection:
        query = insert(State).values(name="Louisiana")
        connection.execute(query)
        query = select([State]).where(State.name == "Louisiana").\
            order_by(State.id.desc())
        states = connection.execute(query)
        print(states.first()[0])

    engine.dispose()
