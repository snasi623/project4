from pprint import pprint
from django.shortcuts import render
from .forms import CreateQuiz, CreateQuestions, TakeQuiz
from .models import Quiz, Question, QuestionResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.forms import modelformset_factory
from django.forms.models import model_to_dict
from django.template.defaulttags import register
import uuid

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
            form.save()
            return redirect(reverse('home'))
    else:
        form = CreateQuestions(initial={'quiz': quiz_pk})

    if 'newquestion' in request.POST:
        form = CreateQuestions(request.POST)
        if form.is_valid():
            form.save()
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

    submission_token = str(uuid.uuid4())
    initial_responses = [] 
    for q in questions:
        initial_responses.append(model_to_dict(QuestionResponse(
            quiz = quiz,
            question = q, 
            selected_option = 1,
            student_name = '',
            submission_token = submission_token
        )))

    if 'submit' in request.POST:
        QuizFormSet = modelformset_factory(QuestionResponse, form=TakeQuiz)
        formset = QuizFormSet(request.POST)

        if formset.is_valid():
            formset.save()
            return redirect(reverse('results', args=(formset[0].instance.submission_token,)))
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
        'submission_token' : submission_token,
    }
    return render(request, 'quiz/quiz.html', context)

def results(request, submission_token):
    results = QuestionResponse.objects.filter(submission_token=submission_token)

    num_correct = 0
    for r in results:
        if r.selected_option == r.question.correct_option:
            num_correct += 1

    grade = round((num_correct / len(results)) * 100)

    context = {'len_results' : len(results), 'num_correct' : num_correct, 'grade' : grade}
    return render(request, 'quiz/results.html', context)

def listresults(request, quiz_pk):
    results = QuestionResponse.objects.filter(quiz_id = quiz_pk)

    dictionary = {}
    for r in results: 
        is_correct = r.selected_option == r.question.correct_option
        if r.submission_token not in dictionary:
            dictionary[r.submission_token] = {
                'len_results': 1,
                'num_correct': int(is_correct),
                'student_name': r.student_name,
                'grade': round((int(is_correct) / 1) * 100)
            }
        else:
            dictionary[r.submission_token]['len_results'] += 1
            dictionary[r.submission_token]['num_correct'] += int(is_correct)
            dictionary[r.submission_token]['grade'] = round((dictionary[r.submission_token]['num_correct'] / dictionary[r.submission_token]['len_results']) * 100)

    context = {'dictionary' : dictionary}
    return render(request, 'quiz/listresults.html', context)