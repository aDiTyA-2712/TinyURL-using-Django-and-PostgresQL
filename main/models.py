from django.db import models

# Create your models here.
class Linker(models.Model):
    original_url = models.CharField(max_length=256)
    hash = models.CharField(max_length=10)
    creation_date = models.DateTimeField('creation date')
    combined_url = models.CharField(max_length=256)
    expiration_date=models.DateTimeField('expiration date', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.combined_url:
            base_url = 'http://127.0.0.1:8000/'
            #base_url = 'http://tinyUrl/'
            self.combined_url = f"{base_url}{self.hash}"    
        super().save(*args, **kwargs)