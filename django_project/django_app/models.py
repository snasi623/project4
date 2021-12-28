from django.db import models

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=40, unique=True)
    tags = models.CharField(max_length=40, unique=True)

class Questions(models.Model):
    question = models.TextField()

class Choices(models.Model):
    option_A = models.CharField(max_length=100, unique=True)
    option_B = models.CharField(max_length=100, unique=True)
    option_C = models.CharField(max_length=100, unique=True)
    option_D = models.CharField(max_length=100, unique=True)

class Answer(models.Model):
    correct_answer = models.CharField(max_length=100, unique=True)
