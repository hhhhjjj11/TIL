from django.shortcuts import render, redirect
from .models import Question, Comment
from .forms import QuestionForm, CommentForm


# Create your views here.
def index(req):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(req, 'eithers/index.html', context)

def create(req):
    if req.method == "POST":
        form = QuestionForm(req.POST)
        if form.is_valid():
            question = form.save()
            return redirect('eithers:detail', question.pk)
    else:
        form = QuestionForm()
        context={
            'form':form
        }
        return render(req, 'eithers/create.html', context)

def random(req):
    question = Question.objects.order_by('?')[0]
    comments = question.comments.all()

    comment_form = CommentForm()
    context= {
        'question':question,
        'comment_form' : comment_form,
        'comments': comments,
    }
    return render(req, 'eithers/detail.html', context)


def detail(req, question_pk):
    question = Question.objects.get(pk=question_pk)
    
    #역참조
    comments = question.comments.all()

    comment_form = CommentForm()
    context= {
        'question':question,
        'comment_form' : comment_form,
        'comments': comments,
    }
    return render(req, 'eithers/detail.html', context)

def comment_create(req, question_pk):
    question = Question.objects.get(pk=question_pk)
    comment_form = CommentForm(req.POST)
    if comment_form.is_valid():
        print('ddd')
        # 유저가 question을 지정하지 않음. 따라서 그 상태로 저장시 참조 게시글 정보가 빠져있음
        # 따라서 따로 처리해줘야함
        comment = comment_form.save(commit=False)
        comment.question = question
        comment.save()
        print('dfsdfsdf')
        return redirect('eithers:detail', question_pk)
    

# 요거는 코드만 넣어놓겠어요.
def comments_delete(req, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)