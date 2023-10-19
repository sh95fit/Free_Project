from database.session.main_db import SessionMain
from database.session.gsrems_db import SessionGsrems


def main_db():
    db = SessionMain()
    try:
        yield db
    finally:
        db.close()


def gsrems_db():
    db = SessionGsrems()
    try:
        yield db
    finally:
        db.close()
