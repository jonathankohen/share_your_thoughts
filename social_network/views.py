from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, Post

def index(req):
    return render(req, "index.html")

def login_page(req):
    return render(req, "login.html")

def register(req):
    validation_errors = User.objects.regValidator(req.POST)
    if len(validation_errors) > 0:
        for key, value in validation_errors.items():
            messages.error(req, value)
        return redirect("/")
    else: 
        pw_hash = bcrypt.hashpw(req.POST['pw'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name = req.POST["first_name"], last_name = req.POST["last_name"], email = req.POST["email"], password = pw_hash)
        req.session['logged_id'] = new_user.id
    return redirect("/home")

def home(req):
    if 'logged_id' not in req.session:
        messages.error(req, "Login required.")
        return redirect('/')
    context = {
        'logged_user': User.objects.get(id = req.session['logged_id']),
        "all_posts": Post.objects.all(),
        "liked_posts": Post.objects.filter(likes= User.objects.get(id = req.session['logged_id'])),
        "other_posts": Post.objects.exclude(likes= User.objects.get(id = req.session['logged_id'])),

    }
    return render(req, 'home.html', context)

def login(req):
    validation_errors = User.objects.loginValidator(req.POST)
    if len(validation_errors) > 0:
        for value in validation_errors.values():
            messages.error(req, value)
        return redirect("/login_page")
    else:
        email_match = User.objects.filter(email = req.POST['email'])
        req.session['logged_id'] = email_match[0].id
        return redirect('/home')

def logout(req):
    req.session.clear()
    return redirect("/")

def add_post(req):
    return render(req, "add_post.html")

def create_post(req):
    validation_errors = Post.objects.post_validator(req.POST)
    if len(validation_errors) > 0:
        for value in validation_errors.values():
            messages.error(req, value)
        return redirect("/add_post")
    Post.objects.create(content = req.POST['post_content'], uploader = User.objects.get(id = req.session['logged_id']))
    return redirect("/home")

def like_post(req, post_id):
    liker = User.objects.get(id = req.session['logged_id'])
    post = Post.objects.get(id = post_id)
    post.likes.add(liker)
    return redirect("/home")

def unlike(req, post_id):
    liker = User.objects.get(id = req.session['logged_id'])
    post = Post.objects.get(id = post_id)
    post.likes.remove(liker)
    return redirect ("/home")

def delete(req, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return redirect("/home")

def show(req, post_id):
    context = {
        "post_object": Post.objects.get(id = post_id)
    }
    return render(req, "show.html", context)

