from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.ArticleList.as_view()),
    path('detail/<int:pk>/', views.ArticleDetail.as_view()),
    #path('g/', views.ArticleList.as_view()),
]

