from sqlalchemy.orm import Session

from app.db_models import Wallet, TransactionRequest

from .settings import COMMISSION


class MakeTransactionHanler():

    def handle(self, sender_id: int, recipient_id: int, amount: float, session: Session) -> dict:

        data = self._collect_data(sender_id, recipient_id, amount, session)

        errors = self._validate(data)

        if errors:

            return errors

        return self._make_transaction(data)

    def _collect_data(self, sender_id: int, recipient_id: int, amount: float, session: Session) -> dict:

        data = {
            'amount': amount,
            'session': session
        }

        data['sender'] = data['session'].query(Wallet).filter_by(id=sender_id).first() 
        data['recipient'] = data['session'].query(Wallet).filter_by(id=recipient_id).first()

        return data

    def _validate(self, data: dict) -> dict:

        if not data['sender']:

            return {'error': 'Sender wallet does not exists'}

        if not data['recipient']:

            return {'error': 'Recipient wallet does not exists'}

        return {}

    def _make_transaction(self, data: dict) -> dict:

        transaction_request =  TransactionRequest(sender=data['sender'], recipient=data['recipient'], amount=data['amount'])

        data['session'].add(transaction_request)
        data['session'].commit()

        amount_after_commission =  data['amount'] * (1 - COMMISSION)
        commission = data['amount'] - amount_after_commission

        data['sender'].balance -= data['amount'] + commission
        data['recipient'].balance +=  amount_after_commission

        data['session'].commit()
    
        return {"success": f"{amount_after_commission} has been successfuly transfered to wallet {data['recipient'].id}"}
