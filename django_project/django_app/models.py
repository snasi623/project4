from django.db import models

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=40, unique=True)
    tags = models.CharField(max_length=40, unique=True)
    question = models.TextField()
    correct_answer = models.CharField(max_length=100, unique=True)
    alt_choice_1 = models.CharField(max_length=100, unique=True)