from django.shortcuts import render
from .forms import CreateQuiz

def index(request):
    context = {}
    return render(request, 'quiz/index.html', context)

def create(request):
    if request.method == 'POST':
        form = CreateQuiz(request.POST)
    else:
        form = CreateQuiz()

    context = {'form' : form}
    return render(request, 'quiz/create.html', context)

def quiz(request):
    context = {}
    return render(request, 'quiz/quiz.html', context)

def results(request):
    context = {}
    return render(request, 'quiz/results.html', context)