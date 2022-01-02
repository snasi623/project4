from django.shortcuts import render
from .forms import CreateQuiz, CreateQuestions, CreateAnswers
from .models import Quiz, Question, Answer
from django.shortcuts import redirect
from django.urls import reverse

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
            return redirect(reverse('createanswers', args=(quiz_pk, created_question.pk)))
    else:
        form = CreateQuestions(initial={'quiz': quiz_pk})

    if 'newquestion' in request.POST:
        form = CreateQuestions(request.POST)
        if form.is_valid():
            created_question = form.save()
            return redirect(reverse('createquestions', args=(quiz_pk,)))
    else:
        form = CreateQuestions(initial={'quiz': quiz_pk})
        pprint.pprint(form.errors)

    if 'back' in request.POST:
        return redirect(reverse('createquiz', args=(quiz_pk)))

    context = {'form' : form, 'question' : question}
    return render(request, 'quiz/createquestions.html', context)

def createanswers(request, quiz_pk, question_pk):
    question = Question.objects.filter(quiz_id = quiz_pk)
    answer = Question.objects.filter(qestion_id = question_pk,)

    if 'submit' in request.POST:
        form = CreateAnswers(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
        else:
            pprint.pprint(form.errors)

    else:
        form = CreateAnswers(initial={'question': quiz_pk})

    context = {'form' : form, 'question' : question, 'answer' : answer}
    return render(request, 'quiz/createanswers.html', context)

def quiz(request, quiz_pk):
    quiz = Quiz.objects.get(pk=quiz_pk)
    question = Question.objects.get(quiz_id=quiz_pk)
    answer = Answer.objects.get(question_id=question.pk)

    context = {
        'quiz' : quiz,
        'question' : question,
        'answer' : answer
    }
    return render(request, 'quiz/quiz.html', context)

def results(request):
    context = {}
    return render(request, 'quiz/results.html', context)