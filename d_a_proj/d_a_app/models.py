from django.db import models
from django.contrib.auth.models import User

# Create your models here.



# model for the blog entries

class BlogModel(models.Model):
    username = models.CharField(max_length=20)
    blogTitle = models.CharField(max_length=20)
    blogEntries = models.TextField(max_length=1000)
    blogAuthor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)


    def __str__(self):
        return self.blogTitle


