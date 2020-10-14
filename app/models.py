from pydantic import BaseModel, ValidationError, root_validator, validator
from typing import List


class TransactionRequestBase(BaseModel):
    
    sender_id: int
    recipient_id: int
    amount: int

    @root_validator
    def check_sender_recipient_not_equal(cls, values):

        sender_id, recipient_id = values.get('sender_id'), values.get('recipient_id')

        if sender_id == recipient_id:

            raise ValueError('Choose different recepient or sender')

        return values

    @validator('amount', pre=True, always=True)
    def check_if_amount_is_positive(cls, value):

        if value < 0:

            raise ValueError('Amount to be sent can not be negative')

        return value
    
    class Config:
        orm_mode = True


class WalletBase(BaseModel):

    name: str
    balance: int

    class Config:
        orm_mode = True
