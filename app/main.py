from fastapi import FastAPI, Depends

from typing import List

from sqlalchemy.orm import Session

from app.models import WalletBase, TransactionRequestBase

from app.db import engine, get_db

from app.db_models import Wallet as WalletModel, TransactionRequest as TransactionRequestModel

from app.functions import MakeTransactionHanler

from .settings import COMMISSION, app


app.state.Base.metadata.create_all(bind=engine)


@app.get("/wallets", response_model=List[WalletBase])
async def wallets_list(session: Session = Depends(get_db)) -> List[WalletBase]:
    
    wallets = session.query(WalletModel).all()

    return wallets

@app.get("/transactions")
async def transactions_list(session: Session = Depends(get_db)) -> List[TransactionRequestBase]:

    transactions = session.query(TransactionRequestModel).all()

    return transactions


@app.post("/transactions")
async def make_transaction(sender_id: int, recipient_id: int, amount: float, db: Session = Depends(get_db)) -> dict:

    result = MakeTransactionHanler().handle(sender_id, recipient_id, amount, db)

    return result
