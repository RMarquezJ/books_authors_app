from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('/createbook', views.createbook),
    path('/addauthor', views.addauthor),
    path('/book/<bookid>', views.bookinfo),
    path('/author/<authorid>', views.authorinfo),
    path('/author/<authorid>/addbook', views.booktoauthor),
]