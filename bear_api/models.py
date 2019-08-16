from django.db import models


class Report(models.Model):
    user = models.CharField(max_length=50)
    tweets = models.IntegerField()
    followers = models.IntegerField()
    following = models.IntegerField()
    verified = models.BooleanField()
    img = models.TextField(default='https://pbs.twimg.com/profile_images/661318201473544192/QYYw4uBv.png')  # nopep8
    description = models.TextField(default=' ')
    url = models.TextField(default='https://twitter.com/home')
    analysis_positive = models.IntegerField()
    analysis_negative = models.IntegerField()
    analysis_neutral = models.IntegerField()
    acceptance_positive = models.IntegerField()
    acceptance_neutral = models.IntegerField()
    acceptance_negative = models.IntegerField()
    created_on = models.DateField(auto_now_add=True)
