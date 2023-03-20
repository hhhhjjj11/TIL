from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(req):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(req, 'articles/index.html', context)

def create(req):
    if req.method == "POST":
        title = req.POST.get('title')
        content = req.POST.get('content')
        article = Article.objects.create(title=title, content = content)
        context={
            'article': article,
        }
        return redirect('articles:index')
    else:
        return render(req, 'articles/create.html')


def detail(req, pk):
    article = Article.objects.get(pk=pk)
    # 삭제
    if req.method == 'POST':
        article.delete()
        return redirect('articles:index')
    # 조회
    elif req.method == 'GET':
        context = {
            'article': article
        }
        return render(req, 'articles/detail.html', context)

def update(req, pk):
    article = Article.objects.get(pk=pk)
    # 수정요청시
    if req.method == 'POST':
        article.title = req.POST.get('title')
        article.content = req.POST.get('content')
        article.save()
        return redirect('articles:detail', pk)
    # 수정화면조회요청시
    elif req.method == 'GET':
        context = {
            'article': article
        }
        return render(req, 'articles/update.html', context)
