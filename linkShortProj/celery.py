# linkShortProj/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'linkShortProj.settings')

app = Celery('main', broker='amqp://guest@localhost/')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
print(app.conf.beat_schedule)
# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.update(
    broker_connection_retry_on_startup=True,
)
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

