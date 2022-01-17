from django.forms import ModelForm, ModelChoiceField, CharField
from django.forms.widgets import HiddenInput
from .models import Quiz, Question, QuestionResponse


class CreateQuiz(ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'category_name', 'instructions']

class CreateQuestions(ModelForm):
    quiz = ModelChoiceField(queryset=Quiz.objects.all(), widget=HiddenInput())

    class Meta:
        model = Question
        fields = ['quiz', 'prompt', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_option']

class TakeQuiz(ModelForm):
    question = ModelChoiceField(queryset=Question.objects.all(), widget=HiddenInput())
    quiz = ModelChoiceField(queryset=Quiz.objects.all(), widget=HiddenInput())
    student_name = CharField(widget = HiddenInput())

    class Meta:
        model = QuestionResponse
        fields = ['quiz', 'question', 'selected_option', 'student_name', 'submission_token']
