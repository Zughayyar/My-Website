from django.db import models
from register.models import User, UserManager

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="comments")
    message = models.ForeignKey(Message,on_delete=models.DO_NOTHING, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def get_user_by_email(email):
    return User.objects.filter(email=email)

def get_all_messages():
    return Message.objects.all().order_by('-created_at')

def create_message(data, user):
    Message.objects.create(
        user = user,
        message = data['message']
    )

def create_comment(data, user):
    message = Message.objects.get(id = data['message_id'])
    Comment.objects.create(
        user = user,
        message = message,
        comment = data['comment']
    )