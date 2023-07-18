from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth import get_user_model
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {'form': form}
    return render(request, 'articles/create.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', pk=article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:detail', article.pk)
    context = {'form': form, 'article': article}
    return render(request, 'articles/update.html', context)

def comments_create(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user= request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')

def comments_delete(request, pk, comment_pk):    
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', pk)

def likes(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    # 이미 좋아요를 누른 게시글이면 좋아요를 해제하면 되고
    # 이미 좋아요를 눌른 게시글이란 말은 중개테이블에 데이터가 존재한단말임.
    # 좋아요를 해제한다는말은 중개테이블의 데이터르 지운다는 말임, remove메서드 이용
    if article.like_users.filter(pk=request.user.pk).exists(): # exists()메서드는 해당 데이터가 존재하는지 안하는지 알려줌
        article.like_users.remove(request.user)

    # 반대로, 좋아요를 누른적이 없으면(중개테이블에 정보없으면) 누른다.(중개테이브에 정보를 만들고 저장한다.)
    else:
        article.like_users.add(request.user)

    return redirect('articles:index')
