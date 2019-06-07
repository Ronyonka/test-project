from django.urls import path

from .views import *


app_name = "articles"


urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('authors/', AuthorView.as_view()),
    path('authors/<int:pk>', AuthorView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view()),
]