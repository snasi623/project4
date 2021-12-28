from django.forms import ModelForm
from .models import Choices, Quiz, Questions, Answer

class CreateQuiz(ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'tags']

class CreateQuestion(ModelForm):
    class Meta:
        model = Questions
        fields = ['question']

class CreateChoices(ModelForm):
    class Meta:
        model = Choices
        fields = ['option_A', 'option_B', 'option_C', 'option_D']

class ChooseCorrectAnswer(ModelForm):
    class Meta:
        model = Answer
        fields = ['correct_answer']