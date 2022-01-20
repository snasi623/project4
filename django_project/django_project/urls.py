from django.contrib import admin
from django.urls import path
from django_app import views as quiz_views


urlpatterns = [
    path('', quiz_views.index, name='home'),
    path('createquiz/', quiz_views.createquiz, name='createquiz'),
    path('createquestions/<int:quiz_pk>', quiz_views.createquestions, name='createquestions'),
    path('quiz/<int:quiz_pk>', quiz_views.quiz, name='quiz'),
    path('results/<str:submission_token>', quiz_views.results, name='results'),
    path('listresults/<int:quiz_pk>', quiz_views.listresults, name='listresults'),
    path('admin/', admin.site.urls),
]