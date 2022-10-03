# from celery import Celery
from ordersscript.celery import app
from quickstart import get_dollar_currency_from_cb

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def update_db():
    get_dollar_currency_from_cb()

