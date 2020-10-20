import os

from fastapi import FastAPI


app = FastAPI()

DATABASE_URL = os.environ["DATABASE_URL"]
COMMISSION = 0.015