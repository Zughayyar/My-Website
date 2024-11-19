from django.db import models
from register.models import User



class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="books", on_delete=models.DO_NOTHING)
    users = models.ManyToManyField(User, related_name="fav_books")