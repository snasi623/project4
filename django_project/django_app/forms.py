from django.forms import ModelForm, ModelChoiceField, MultipleHiddenInput
from django.forms.widgets import HiddenInput
from .models import Quiz, Question, Answer

class CreateQuiz(ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'category_name']

class CreateQuestions(ModelForm):
    quiz = ModelChoiceField(queryset=Quiz.objects.all(), widget=HiddenInput())

    class Meta:
        model = Question
        fields = ['quiz', 'prompt']

class CreateAnswers(ModelForm):
    question = ModelChoiceField(queryset=Question.objects.all(), widget=HiddenInput())

    class Meta:
        model = Answer
        fields = ['question', 'answer_text']