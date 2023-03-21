from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(req):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(req, 'articles/index.html', context)

def create(req):
    if req.method == "POST":
        form = ArticleForm(req.POST)
        if form.is_valid(): # 입력된 폼이 유효하다면
            article = form.save()
            return redirect('articles:detail', article.pk)
        return redirect('articles:create')
        # title = req.POST.get('title')
        # content = req.POST.get('content')
        # article = Article.objects.create(title=title, content = content)
        # context={
        #     'article': article,
        # }
        # return redirect('articles:index')
    else:
        form = ArticleForm()
        context = {'form': form }
        return render(req, 'articles/create.html', context)


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
        form = ArticleForm(req.POST, instance = article)
        if form.is_valid():
            form.save()
            return redirect('article:detail', pk=article.pk)
        
        # article.title = req.POST.get('title')
        # article.content = req.POST.get('content')
        # article.save()
        #return redirect('articles:detail', pk)
    # 수정화면조회요청시
    elif req.method == 'GET':
        form = ArticleForm(instance = article)

        # context = {
        #     'article': article
        # }
    context = {'form': form}
    return render(req, 'articles/update.html', context)
