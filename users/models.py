from django.db import models


class User(models.Model):
    email = models.TextField()
    password = models.TextField()
    # author = models.CharField(max_length=50)
    # genre = models.CharField(max_length=20)
    # description = models.TextField()

    def __str__(self):
        return self.email
