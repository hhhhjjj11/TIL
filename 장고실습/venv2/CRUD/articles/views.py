from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def index(req):
    articles = Article.objects.all()
    context ={
        'articles': articles
    }
    return render(req, 'articles/index.html', context)

def detail(request, id):
    # 참고 id는 걍 pk 로써줘도 장고가 알아서 알아 먹는다.
    # 둘다 상관 없다 그래서.
    # article = Article.objects.get(id=pk)
    # article = Article.objects.get(pk=pk)
    article = Article.objects.get(pk=id)
    context = {'article' :article }
    return render(request, 'articles/detail.html', context)

def new(req):
    return render(req, 'articles/new.html')

def create(req):
    title = req.POST.get('title')
    content = req.POST.get('content')

    # article = Article.objects.create(title=title,content=content)

    article = Article(title=title, content=content)
    article.save()

    context={
        'createdData' : article
    }
    return redirect('articles:index')