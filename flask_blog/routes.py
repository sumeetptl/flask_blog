from flask_blog.models import User, Post
from flask import render_template, url_for, flash, redirect
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog import app


posts = [
    {
        'author':'Rucha Butala',
        'title':'First blog post',
        'content':'Rucha blog contents',
        'date_posted':'November 1, 1996'
    },
    {
        'author':'Sumeet Patil',
        'title':'Second blog post',
        'content':'Sumeet blog contents',
        'date_posted':'November 2, 2021'
    }
]

@app.route("/")
@app.route("/home/")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about/")
def about():
    return render_template('about.html',title='About')


@app.route("/register/", methods=['GET', 'POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for { form.username.data }!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)


@app.route("/login/",methods=['GET','POST'])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)