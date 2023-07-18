from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    # user라는 필드명으로, User모델과의 관계가 저장된다.
    # 
    # "좋아한유저"라는 필드명으로, 이 
    # 1:M일때는 M에다가 필드를 만든다 1에다가 필드를 만들면 안된다.
    # 그래서 게시글- 댓글은 1:N이므로 (게시글1개, 댓글여러개) 댓글에다가 article 외래키를 만든다.
    # M:N일때는 뭐 상관없는데 통상적으로 쩌리한테 만드는듯?
    # 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
