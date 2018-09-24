from __future__ import absolute_import, unicode_literals
from celery import shared_task
from politik.models import Politician, LawProject

@shared_task
def task_number_one():
    print("bakljklajskld")
    return '{} random users created with success!'