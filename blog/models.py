from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # models.ForeignKey : 다른 모델에 대한 링크
    title = models.CharField(max_length=200) # models.CharField : 짧은 문자열
    text = models.TextField() # models.TextField : 긴 텍스트
    created_date = models.DateTimeField( # models.DateTimeField : 날짜와 시간
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
