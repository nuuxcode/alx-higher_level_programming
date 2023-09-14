#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select, text

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    state_name = MySQLdb.escape_string(sys.argv[4])
    with engine.connect() as connection:
        query = select([State]) \
            .where(text("name = :name").bindparams(name=state_name))
        states = list(connection.execute(query, state_name=state_name))
        if states:
            for state in states:
                print(state[0])
        else:
            print("Not found")

    engine.dispose()
