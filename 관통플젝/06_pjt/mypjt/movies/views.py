from django.shortcuts import render, redirect
from .models import Movie,Comment
from .forms import CommentForm, MovieForm


def index(req):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(req, 'movies/index.html', context)

def create(req):
    if req.method=="POST":
        if not req.user.is_authenticated:
            return redirect('accounts:login')
        form = MovieForm(req.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user_id= req.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    
    form = MovieForm()
    context ={
        'form':form
    }
    return render(req, 'movies/create.html', context)

def detail(req, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment_form = CommentForm()
    commetns = movie.comment_set.all()
    context = {
        'movie': movie,
        'comment_form':comment_form,
        'comments':commetns,
    }
    return render(req, 'movies/detail.html',context)

def update(req, movie_pk):
    if not req.user.is_authenticated:
        return redirect('movies:detail', movie_pk)
    
    movie = Movie.objects.get(pk=movie_pk)
    if req.method == "POST":
        if req.user == movie.user_id:
            form = MovieForm(req.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie_pk)
        else: 
            return redirect('movies:detail', movie_pk)
    form = MovieForm(instance=movie)    
    context ={
        'form':form,
        'movie':movie
    }
    return render(req, 'movies/update.html', context)

def delete(req, movie_pk):
    
    movie = Movie.objects.get(pk=movie_pk)
    if req.user == movie.user_id:
        movie.delete()
    else:
        return redirect('movies:detail',movie_pk)
    
    return redirect(req, 'movies:index')

def comments_create(req, movie_pk):
    if not req.user.is_authenticated:
        redirect('movies:detail', movie_pk)
    movie = Movie.objects.get(pk=movie_pk)
    comment_form = CommentForm(req.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie_id = movie
        comment.user_id = req.user 
        comment.save()
    
    return redirect('movies:detail', movie_pk)

def comments_delelte(req, movie_pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    if req.user == comment.user_id:
        comment.delete()
    redirect('movies:detail',movie_pk)

def likes(req, movie_pk):
    if req.user.is_authenticated:    
        movie = Movie.objects.get(pk=movie_pk)
        if movie.user_liked.filter(pk=req.user.pk).exists():
            movie.user_liked.remove(req.user)
        else:
            movie.user_liked.add(req.user)
        return redirect('movies:index')
    return redirect('accoutns:login')