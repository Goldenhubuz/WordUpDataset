from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class Word(TimeStampedModel):
    text = models.CharField(max_length=50, unique=True)
    transcription = models.CharField(max_length=50, unique=True)
    definition = models.CharField(max_length=255, unique=True)
    sentence = models.CharField(max_length=255, unique=True)