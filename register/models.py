from django.db import models
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, data):
        errors = {}
        




class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def create_user(data):
    password =data['password']
    hashed_pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(
        first_name = data['first_name'],
        last_name = data['last_name'],
        email = data['email'],
        password = hashed_pwd
    )

def is_user_exist(data):
    users = User.objects.filter(email = data['email'])
    if len(users) == 0:
        return False
    else:
        return True

def get_user_by_email(email):
    return User.objects.filter(email=email)

def is_password_match(entered_email, entered_password):
    user = User.objects.filter(email = entered_email)
    password = user[0].password
    return bcrypt.checkpw(entered_password.encode() , password.encode())

def check_login(data):
    entered_email = data['email']
    entered_password = data['password']
    return is_password_match(entered_email,entered_password)
