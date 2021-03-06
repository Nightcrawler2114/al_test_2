FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt 

COPY . /app

WORKDIR /app
ADD . /app

ENV DATABASE_URL="postgresql://superuser:superuser@postgresql:5432/al-test-3" 

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
