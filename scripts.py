from fastapi import Depends

from sqlalchemy.orm import Session

from app.db import get_db, get_db_session
from app.db_models import Wallet


def main():

    session = get_db_session()

    session.add(Wallet(name='test', balance=10))
    session.add(Wallet(name='test1', balance=15))
    session.add(Wallet(name='test2', balance=25))

    session.commit()

    wallets = session.query(Wallet).all()

    print(wallets)


if __name__ == '__main__':
    
    main()