from database.session.auth_db import Session


def auth_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
