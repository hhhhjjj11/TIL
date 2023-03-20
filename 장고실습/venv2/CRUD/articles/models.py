from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content= models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # auto_now vs auto_now_add
    # 후자는 생성시간 전자는 수정시간

    # 매직메서드 오버라이딩
    def __str__(self):
        return f'{self.id}번째 글 - {self.title}'