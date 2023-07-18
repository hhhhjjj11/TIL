from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import ArticleSerializer
from .models import Article, Comment
from rest_framework.response import Response
from rest_framework import status # 상태코드를 내가 정해주고 싶을 때


# 유라시간에 했던. json응답 방법4가지
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers

def article_html(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title' : article.title,
                'content':article.content,
            }
        )
    
    return JsonResponse(articles_json, safe=False)


def article_json_2(request):
    articles = Article.objects.all()
    data= serializers.serialize('json', articles) # json형태로 articles를 직렬화한후 반환
    return HttpResponse(data, content_type = 'application/json')


@api_view(['GET'])
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many = True) # many 는 아티클 인스턴스 여러개 한번에 받는거 허용하는 설정임. 여러개 줄테니 알아서 직렬화 해서 반환해줘~ 
    return Response(serializer.data) 



# 여기부터는 반에서 수업 한거

# 전체 조회, 생성
# @api_view: 함수가 API View로 동작하도록 변환
#   - 메소드 제한 가능
#   - HttpResponse 대신 Json이나 DRF의 Response 객체 반환 가능

@api_view(['GET','POST'])
def article_list(req):
    if req.method=="POST":
        # 시리얼라이즈는 폼과 쓰는게 되게 비슷함!
        # form = ArticleForm(req.POST)
        serializer = ArticleSerializer(data = req.data)
        if serializer.is_valid(raise_exception=True): # raise-exception : 유효성 검사 실패시 자동으로 에러를 반환해줌
            serializer.save()
            return Response(serializer.data)
        
    # GET이라면
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles,many=True)

    return Response(serializer.data)

# 상세 조회, 수정, 삭제
@api_view(['GET','PUT','DELETE'])
def article_detail(req,pk):
    article = get_object_or_404(Article, pk=pk) # get_object_or_404를  써야  데이터가 없어도 에러가 안뜨고 없다는 문구로 뜸.
    
    if req.method == "PUT":
        # 수정시에도 폼과 비슷함. 기존데이터를 폼의 첫번째 인자로 넣어줬던것처럼, 시리얼라이즈에서도 첫 번째 인자로 인스턴스를 넣어준다는 점.
        serializer = ArticleSerializer(article, data = req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif req.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # GET이라면
    serializer = ArticleSerializer(article)

    return Response(serializer.data)
