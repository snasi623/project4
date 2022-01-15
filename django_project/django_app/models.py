from django.db import models
import uuid

class Quiz(models.Model):
    name = models.CharField(max_length=40, default='')
    category_name = models.CharField(max_length=40, default='')
    instructions = models.TextField(default='')

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    prompt = models.TextField(default='')
    option_1 = models.CharField(max_length=200, default='')
    option_2 = models.CharField(max_length=200, default='')
    option_3 = models.CharField(max_length=200, default='')
    option_4 = models.CharField(max_length=200, default='')
    correct_option = models.PositiveSmallIntegerField(choices=[
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
    ], default=1)

class QuestionResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.PositiveSmallIntegerField(choices=[
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
    ], default=1)
    student_name = models.CharField(max_length=50, default='')
    submission_token = models.CharField(max_length=255, default=str(uuid.uuid4()))