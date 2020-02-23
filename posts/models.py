from django.db import models


# Create your models here.
class User(models.Model):
    """作者"""
    username = models.CharField(max_length=128)


class Topic(models.Model):
    """专题"""
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Post(models.Model):
    """文章"""
    title = models.CharField(max_length=128)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)

    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topic, blank=True)

    class Meta:
        ordering = ['-created']

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.__repr__()
