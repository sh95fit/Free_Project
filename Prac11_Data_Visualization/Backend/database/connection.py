from database.session.more_db import Session

def more_db() :
    db = Session()
    try:
        yield db
    finally:
        db.close()

