from django.db import models
from users.models import User

class Keyword(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=120)
    text = models.CharField(max_length=250)
    video_link = models.CharField(max_length=250)
    photo_link = models.CharField(max_length=250)
    keywords = models.ManyToManyField(Keyword, null=True)
    publishedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    view = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title

class Categories(models.Model):
    name = models.CharField(max_length=50)
    link = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class VideoOTD(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)

    def __str__(self)->str:
        return self.video.name