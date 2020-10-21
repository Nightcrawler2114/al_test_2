from fastapi import Depends

from sqlalchemy.orm import Session

from app.db import get_db, get_db_session
from app.db_models import Wallet


def main():

    session = get_db_session()

    session.add(Wallet(id=1, name='test', balance=10))
    session.add(Wallet(id=2,name='test1', balance=15))
    session.add(Wallet(id=3,name='test2', balance=25))
    session.add(Wallet(id=4,name='test3', balance=35))

    session.commit()

    wallets = session.query(Wallet).all()

    print(wallets)


if __name__ == '__main__':
    
    main()