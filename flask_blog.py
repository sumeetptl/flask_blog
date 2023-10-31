from flask import Flask, render_template, url_for
from .forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='ba74618dda4152eae64241362a2e862b'

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


@app.route("/register/")
def register():
    form= RegistrationForm()
    return render_template('register.html',title='Register')


@app.route("/login/")
def login():
    form= LoginForm()
    return render_template('login.html',title='Login')


if __name__ == '__main__':
    app.run(debug=True)