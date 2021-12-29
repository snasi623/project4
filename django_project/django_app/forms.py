from django.forms import ModelForm
from .models import Quiz

class CreateQuiz(ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'tags', 'question', 'correct_answer', 'alt_choice_1']
