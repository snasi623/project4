from django.shortcuts import render
from .forms import CreateQuiz, CreateQuestions, TakeQuiz
from .models import Quiz, Question, QuestionResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.forms import formset_factory

import pprint


def index(request):
    quiz = Quiz.objects.all()
    tags = list(set(x.category_name for x in quiz))

    context = { 
        'quiz' : quiz, 
        'tags' : tags 
    }
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
    try:
        question = Question.objects.filter(quiz_id = quiz_pk)
    except Question.DoesNotExist:
        question = None

    if 'next' in request.POST:
        form = CreateQuestions(request.POST)
        if form.is_valid():
            created_question = form.save()
            return redirect(reverse('home'))
    else:
        form = CreateQuestions(initial={'quiz': quiz_pk})

    if 'newquestion' in request.POST:
        form = CreateQuestions(request.POST)
        if form.is_valid():
            created_question = form.save()
            return redirect(reverse('createquestions', args=(quiz_pk,)))
    else:
        form = CreateQuestions(initial={'quiz': quiz_pk})

    context = {'form' : form, 'question' : question}
    return render(request, 'quiz/createquestions.html', context)

def quiz(request, quiz_pk):
    quiz = Quiz.objects.get(pk=quiz_pk)
    question = Question.objects.filter(quiz_id=quiz_pk)

    try:
        question = Question.objects.filter(quiz_id = quiz_pk)
    except Question.DoesNotExist:
        question = None

    formset = formset_factory(QuestionResponse)()
    
    if 'submit' in request.POST:
        form = TakeQuiz(request.POST)
        if form.is_valid():
            return redirect(reverse('results'))
        else: 
            pprint.pprint(form.errors)
    else:
        form = TakeQuiz(initial={'quiz': quiz_pk})

    context = {
        'form' : form,
        'quiz' : quiz,
        'formset': formset,
        'question' : question,
    }
    return render(request, 'quiz/quiz.html', context)

def results(request, quiz_id):
    results = QuestionResponse.objects.get(pk=quiz_id)

    context = {'results' : results}
    return render(request, 'quiz/results.html', context)