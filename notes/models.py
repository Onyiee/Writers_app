from django.db import models


# Create your models here.
class Tweet(models.Model):
    tweet_date = models.DateTimeField(auto_now_add=True)
    tweet_body = models.TextField()

    def __str__(self):
        return self.tweet_body
