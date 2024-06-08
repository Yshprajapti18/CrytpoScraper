from django.db import models

# Create your models here.

from django.db import models
import uuid
from django.db.models import JSONField

class ScrapingJob(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    coins = models.JSONField()  # List of coin names
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

class CoinData(models.Model):
    job = models.ForeignKey(ScrapingJob, related_name='coins_data', on_delete=models.CASCADE)
    coin = models.CharField(max_length=50)
    data = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

