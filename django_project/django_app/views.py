from django.shortcuts import render
from .forms import CreateQuiz

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        form = CreateQuiz(request.POST)
    else:
        form = CreateQuiz()

    context = {'form' : form}
    return render(request, 'create.html', context)

def quiz(request):
    context = {}
    return render(request, 'quiz.html', context)

def score(request):
    context = {}
    return render(request, 'score.html', context)