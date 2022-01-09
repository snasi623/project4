from django.shortcuts import render
from .forms import CreateQuiz, CreateQuestions, TakeQuiz
from .models import Quiz, Question, QuestionResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.forms import modelformset_factory
from django.forms.models import model_to_dict
from django.template.defaulttags import register

import pprint

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

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

    try:
        questions = Question.objects.filter(quiz_id = quiz_pk)
    except Question.DoesNotExist:
        questions = None

    initial_responses = [] 
    for q in questions:
        initial_responses.append(model_to_dict(QuestionResponse(
            question = q, 
            selected_option = 1,
            student_name = "Sean"
        )))
    pprint.pprint(initial_responses)

    if 'submit' in request.POST:
        QuizFormSet = modelformset_factory(TakeQuiz)
        formset = QuizFormSet(request.POST)   
        if formset.is_valid():
            return redirect(reverse('results'))
        else: 
            pprint.pprint(formset.errors)
    else:
        QuizFormSet = modelformset_factory(QuestionResponse, form=TakeQuiz, extra=len(initial_responses))
        formset = QuizFormSet(queryset=QuestionResponse.objects.none(), initial=initial_responses)

    context = {
        'quiz' : quiz,
        'formset' : formset,
        'questions' : {x.pk:x for x in questions},
        'initial_responses' : initial_responses,
    }
    return render(request, 'quiz/quiz.html', context)

def results(request, quiz_id):
    results = QuestionResponse.objects.get(pk=quiz_id)

    context = {'results' : results}
    return render(request, 'quiz/results.html', context)