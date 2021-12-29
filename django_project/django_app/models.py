from django.db import models

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=40, default='')
    category_name = models.CharField(max_length=40, default='')
    instructions = models.TextField(default='')

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    prompt = models.TextField(default='')

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200, default='')
    is_correct = models.BooleanField(default=False)

class Response(models.Model):
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
