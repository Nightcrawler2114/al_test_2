from sqlalchemy.exc import OperationalError

from app.db import get_db, get_db_session
from app.db_models import Wallet

import time
import os


def main():

    session = get_db_session()

    id = 1
    created = 0

    while created <= 4:
        
        if session.query(Wallet).filter_by(id=id).first():
            
            id += 1
            
            continue

        session.add(Wallet(id=id, name=f'test{id}', balance=30))
        session.commit()

        created += 1
        
    wallets = session.query(Wallet).all()

    print(wallets)


if __name__ == '__main__':
    
    while True:
        try:
            main()
            break
        except OperationalError:
            time.sleep(10)

    os.system('uvicorn app.main:app --reload')