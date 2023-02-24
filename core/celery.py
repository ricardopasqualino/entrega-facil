from celery import Celery
from tasks import add 
from delivery.models import morador 

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y




def nova_entrega(morador):
    email = morador.email
    return(email)
