from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie

def index(request):
  movie = Movie.objects.all()

  context = {
      'movies' : movie, 
      'saludo': 'Hola'
  }
  return render(request, 'index.html', context)


def create(request):
  tit = request.POST["tit"]
  yea = request.POST["yea"]
  dur = request.POST["dur"]
  des = request.POST["des"]

  Movie.objects.create(title=f'{tit}', description=f'{des}', release_date=f'{yea}', duration=f'{dur}')

  return redirect('/')

def dojo(request):
  return HttpResponse('ninja')