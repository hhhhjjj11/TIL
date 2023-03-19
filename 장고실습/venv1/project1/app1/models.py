from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    content2 = models.TextField()

    # 클래스가 호출되면 __str__이 저절로 호출됨. 그래서 이거를 재정의 해주면 클래스가 호출될때
    # 원하는 값들을 자동으로 리턴해줄 수 있다.
    def __str__(self):
        return f'{self.title} / {self.content} / {self.content2}'