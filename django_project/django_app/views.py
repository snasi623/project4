from django.shortcuts import render
from .forms import CreateQuiz, CreateQuestions, CreateAnswers
from .models import Quiz
from django.shortcuts import redirect
from django.urls import reverse

import pprint


def index(request):
    quiz = Quiz.objects.all()

    context = { 'quiz' : quiz }
    return render(request, 'quiz/index.html', context)

def createquiz(request):
    if request.method == 'POST':
        form = CreateQuiz(request.POST)
        if form.is_valid():
            created_quiz = form.save()

            return redirect(reverse('createquestions', args=(created_quiz.pk,)))

    else:
        form = CreateQuiz()

    context = {'form' : form}
    return render(request, 'quiz/createquiz.html', context)

def createquestions(request, quiz_pk):
    if request.method == 'POST':
        form = CreateQuestions(request.POST)

        if form.is_valid():
            created_question = form.save()

            return redirect(reverse('createanswers', args=(quiz_pk, created_question.pk)))
        else:
            pprint.pprint(form.errors)

    else:
        form = CreateQuestions(initial={'quiz': quiz_pk})

    context = {'form' : form}
    return render(request, 'quiz/createquestions.html', context)

def createanswers(request, quiz_pk, question_pk):
    if request.method == 'POST':
        form = CreateAnswers(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
        else:
            pprint.pprint(form.errors)

    else:
        form = CreateAnswers(initial={'question': question_pk})

    context = {'form' : form}
    return render(request, 'quiz/createanswers.html', context)

def quiz(request):
    context = {}
    return render(request, 'quiz/quiz.html', context)

def results(request):
    context = {}
    return render(request, 'quiz/results.html', context)