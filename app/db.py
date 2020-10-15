from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings import DATABASE_URL, app

engine = create_engine(DATABASE_URL)

app.state.Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app.state.Base = declarative_base()


# Dependency
def get_db():
    db = app.state.Session()
    try:
        yield db
    finally:
        db.close()