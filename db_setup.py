from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from db_models import Base

def db_setup():
    engine = create_engine('sqlite:///lmb.db')

    @event.listens_for(engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

if __name__ == "__main__":
    db_setup()
