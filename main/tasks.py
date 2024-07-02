import logging
from celery import shared_task
from django.utils import timezone
from .models import Linker

logger = logging.getLogger(__name__)

@shared_task
def delete_expired_urls():
    '''logger.info("Running delete_expired_urls task")
    now = timezone.now()
    expired_urls = Linker.objects.filter(expiration_date__lt=now)
    logger.info(f"Found {expired_urls.count()} expired links to delete")
    expired_urls.delete()
    logger.info("Expired links deleted")'''
    now = timezone.now()
    expired_urls = Linker.objects.filter(expiration_date__lt=now)
    expired_urls.delete()
