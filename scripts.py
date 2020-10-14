from app.db import get_db
from app.db_models import Wallet


def main(session: Session = Depends(get_db)):

    session.add(Wallet(name='test', balance=10))
    session.add(Wallet(name='test1', balance=15))
    session.add(Wallet(name='test2', balance=25))

    wallets = session.query(Wallet).all()

    print(wallets)


if __name__ == '__main__':
    
    main()