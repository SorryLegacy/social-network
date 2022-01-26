from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Name')
    slug = models.SlugField(verbose_name='SLug', unique=True)
    description = models.TextField(verbose_name='Text')

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='text')
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text


