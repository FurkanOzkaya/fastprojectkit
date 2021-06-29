FROM python:3.8
ENV PYTHONBUFFERED 1

RUN mkdir /app
WORKDIR /app

EXPOSE 8000

COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]