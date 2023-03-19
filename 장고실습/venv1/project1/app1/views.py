from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def test1(req):
    return render(req, 'app1/test1.html')

def variableRouting(req, num1, num2):
    sum = num1 + num2
    context ={
        'sum':sum
    }
    
    return render(req, 'app1/variableRouting.html', context)

def throw(req):
    return render(req, 'app1/throw.html')

def catch(req):
    message = req.POST.get('throw')
    context ={
        'message':message
    }
    return render(req, 'app1/catch.html', context)

def create(req):
    return render(req, 'app1/create.html')
    
def new(req):
    title = req.POST.get('title')
    content = req.POST.get('content')
    newData = Article.objects.create(title=title,content=content)
        
    return redirect('app1:test')
    
# 질문 : 같은 url에 대해서 다른요청(get or post)을 할 수 있는거 아닌가?
# 이처럼 같은 url에 대한 다른 요청들 처리 분기 어떻게 하지?

def articles(req):
    articles = Article.objects.all()
    context={
        'articles': articles,
    }

    return render(req, 'app1/articles.html', context)