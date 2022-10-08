import os
from deta import _Base, Deta

def connect_to_deta_db(db_name: str) -> _Base:
    DETA_PROJECT_KEY = os.environ['DETA_PROJECT_KEY']
    deta = Deta(DETA_PROJECT_KEY)
    return deta.Base(db_name)
