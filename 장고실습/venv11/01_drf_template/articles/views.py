from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Article, Comment
from .serializers import ArticleListSerializer, CommentSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleListSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            # raise_exception = True // 유효성 검사 실패시 400상태코드 반환.
            serializer.save()
            return Response( status =status.HTTP_201_CREATED )


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleListSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializers = CommentSerializer(comments, many = True)
        return Response(serializers.data)

    elif request.method == 'POST':
        pass

@api_view(['GET'])
def comment_detail(request, comment_pk):
    if request.method == 'GET':
        comment =Comment.objects.get(pk=comment_pk)
        serializers = CommentSerializer(comment)
        return Response(serializers.data)

@api_view(['POST'])
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializers = CommentSerializer(data = request.data)
    if serializers.is_valid(raise_exception=True):
        serializers.save(article = article)
        return Response(serializers.data, status = status.HTTP_201_CREATED)
    