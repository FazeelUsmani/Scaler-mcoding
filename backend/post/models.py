from django.db import models
from datetime import time

# Create your models here.


class Post(models.Model):
    postid = models.AutoField(primary_key=True)
    post_text = models.CharField(max_length=120)
    author_id = models.IntegerField()
    author_name = models.CharField(max_length=24)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.postid} {self.post_text} {self.author_id} {self.author_name} {timestamp}"


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_text = models.CharField(max_length=50)
    author_name = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text


class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    # author_name = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
