# -*- encoding=UTF-8 -*-

from nowstagram import app
from flask import render_template, redirect
from models import Image, User


@app.route('/')
def index():
    images = Image.query.limit(10).all()
    return render_template('index.html', images=images)

@app.route('/image/<int:image_id>/')
def image(image_id):
    image= Image.query.get(image_id)
    if image == None:
        return redirect('/')
    return render_template('pageDetail.html', image=image)

@app.route('/profile/<int:user_id>/')
def profile(user_id):
    user= User.query.get(user_id)
    if user == None:
        return redirect('/')
    return render_template('profile.html', user=user)

@app.route('/login')
def login():
    return render_template('login.html')