from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def regValidator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data["first_name"]) == 0:
            errors['first_name_required'] = "First name is required."
        if len(post_data["last_name"]) == 0:
            errors['last_name_required'] = "Last name is required."

        if len(post_data["email"]) == 0:
            errors['email_required'] = "Email is required."
        elif not EMAIL_REGEX.match(post_data['email']):
            errors['invalid_email'] = "Please enter a valid email."
        else: 
            duplicate_email = User.objects.filter(email = post_data['email'])
            if len(duplicate_email) > 0:
                errors['duplicate_email'] = "This email is already in the database."

        if len(post_data["pw"]) < 4:
            errors['pw_required'] = "Password must be at least 4 characters long."
        if post_data["pw"] != post_data["c_pw"]:
            errors['c_pw_required'] = "Passwords must match."
        return errors

    def loginValidator(self, post_data):
        errors = {}
        email_match = User.objects.filter(email = post_data['email'])

        if len(post_data['email']) == 0:
            errors['email_required'] = "Please enter your login email."
        elif len(email_match) == 0:
            errors['email_404'] = "Invalid email."
        else:
            user_check = email_match[0]
            if bcrypt.checkpw(post_data['pw'].encode(), email_match[0].password.encode()):
                print("Password match")
            else:
                errors['pw_check'] = "Please enter a valid password."
        return errors

class PostManager(models.Manager):
    def post_validator(self, post_data):
        errors = {}
        if len(post_data["post_content"]) < 5:
            errors["post_length"] = "Minimum length five characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Post(models.Model):
    content = models.TextField()
    uploader = models.ForeignKey(User, related_name = "posts_uploaded", on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name = "posts_liked")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = PostManager()