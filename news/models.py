from django.db import models
from django.conf import settings # 유저모델을 가져오는 것.
from django.contrib.auth.models import AbstractUser # 커스텀 유저 모델

# Create your models here.
class Category(models.Model):
    name = models.TextField()
    inter_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='inter_cate', blank=True)
    
    def __str__(self):
        return self.name

class Keyword(models.Model):
    name = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class KeyNews(models.Model):
    title = models.TextField()
    content = models.TextField()
    url = models.TextField()
    date = models.IntegerField()
    keyword = models.ForeignKey(Keyword, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class RankNews(models.Model):
    title = models.TextField()
    content = models.TextField()
    url = models.TextField()
    date = models.IntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete = models.CASCADE)

    def __str__(self):
        return self.content
