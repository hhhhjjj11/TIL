from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieModelForm
from django.views.decorators.http import require_http_methods
# Create your views here.

@require_http_methods(['GET'])
def index(req):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(req, 'movies/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(req):
    if req.method=="POST":
        form = MovieModelForm(req.POST, req.FILES)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk )
    else:
        form = MovieModelForm()
        context ={
            'form':form
        }
        return render(req, 'movies/create.html', context)

@require_http_methods(['GET', 'POST'])
def update(req, pk):
    movie = Movie.objects.get(pk=pk)
    if req.method=="POST":
        form = MovieModelForm(req.POST, instance=movie)

        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieModelForm()
        context={
            'movie':movie,
            'form':form,
        }
        return render(req,'movies/update.html', context)

@require_http_methods(['GET'])
def detail(req, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }
    return render(req, 'movies/detail.html', context)


@require_http_methods(['POST'])
def delete(req, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')