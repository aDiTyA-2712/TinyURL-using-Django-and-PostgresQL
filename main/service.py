import random
import string
from django.utils import timezone
from .models import Linker
from datetime import timedelta

def shorten(url):
    random_hash = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
    creation_date=timezone.now()
    expiration_date=creation_date+timedelta(hours=1)
    mapping = Linker(original_url=url, hash=random_hash, creation_date=creation_date,expiration_date=expiration_date)
    mapping.save()
    return random_hash
 

def load_url(url_hash):
    return Linker.objects.get(hash=url_hash)