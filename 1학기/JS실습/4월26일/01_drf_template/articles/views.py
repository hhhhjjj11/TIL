from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleListSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.data)
        serializer = ArticleListSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == "GET":
        print(request.GET)
        print(request.data)
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)        
        return Response(serializer.data)
    
@api_view(['GET'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleListSerializer(article)
    return Response(serializer.data)
