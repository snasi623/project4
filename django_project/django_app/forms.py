from django.forms import ModelForm
from .models import Quiz
from .models import Choices
from .models import Answer

# class CreateQuiz(ModelForm):
#     class Meta:
#         model = Quiz, Choices
#         fields = ['question', 'option_A', 'option_B', 'option_C', 'option_D']