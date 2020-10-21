import pytest

from typing import List

from fastapi.testclient import TestClient
from fastapi import Depends
from sqlalchemy.orm import Session

from .models import *
from .exceptions import *
from .settings import COMMISSION
from .db import get_db, get_db_session

from .main import test_app


client = TestClient(test_app)


def test_wallets_list():

    response = client.get("/wallets")
    
    assert response.status_code == 200

def test_transaction_list():

    response = client.get("/transactions")

    assert response.status_code == 200

def test_make_transaction():

    # testing with recipient does not exists
    data = {
        'sender_id': 1, 
        'recipient_id': 1123213, 
        'amount': 10
    }

    with pytest.raises(WalletNotFoundException):

        response = client.post(
            "/transactions",
            params=data 
        )

    # testing with sender does not exists
    data = {
        'sender_id': 11231232, 
        'recipient_id': 1, 
        'amount': 10
    }

    with pytest.raises(WalletNotFoundException):

        response = client.post(
            "/transactions",
            params=data 
        )

    # testing with recipient and sender being the same 
    data = {
        'sender_id': 3, 
        'recipient_id': 3, 
        'amount': 10
    }

    with pytest.raises(ValueError):

        response = client.post(
            "/transactions",
            params=data 
        )

    # testing with negative amount
    data = {
        'sender_id': 3, 
        'recipient_id': 4, 
        'amount': -10
    }

    with pytest.raises(ValueError):
        response = client.post(
            "/transactions",
            params=data 
        )

    # testing with insuficient funds
    data = {
        'sender_id': 3, 
        'recipient_id': 4, 
        'amount': 999999999
    }

    with pytest.raises(InsufficientFundsException):
        response = client.post(
            "/transactions",
            params=data 
        )

        print('!!!', response.json())

    # testing with all data being valid
    data = {
        'sender_id': 3, 
        'recipient_id': 4, 
        'amount': 5
    }

    response = client.post(
        "/transactions",
        params=data 
    )

    assert response.status_code == 200
    assert response.json() == {"success": f"{data['amount'] - (data['amount'] - data['amount'] * (1 - COMMISSION))} has been successfuly transfered to wallet {data['recipient_id']}"}

