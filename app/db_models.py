from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.settings import app


class Wallet(app.state.Base):   

    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    balance = Column(Float)

    def __repr__(self) -> str:
        return f'Wallet: "{self.name}/{self.id}"; Available funds: {self.balance}'


class TransactionRequest(app.state.Base):

    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('wallets.id'))
    recipient_id = Column(Integer, ForeignKey('wallets.id'))
    amount = Column(Float)

    sender = relationship("Wallet", foreign_keys=[sender_id])
    recipient = relationship("Wallet", foreign_keys=[recipient_id])

    def __repr__(self) -> str:
        return f'Request ID:{self.id}; Amount: {self.amount}'

