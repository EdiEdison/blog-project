from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=10)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    location = models.CharField(max_length=9, help_text='e.g Buea Town')
    date_posted = models.DateTimeField()
    content = models.TextField()
    author_name = models.CharField(max_length=20, default='put your name in here')

    def __str__(self):
        return self.location


