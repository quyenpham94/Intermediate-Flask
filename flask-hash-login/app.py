from flask import Flask, render_template, redirect, session, flash
from models import connect_db, db, User
from forms import UserForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///auth_demo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ihaveasecret'
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/tweets')
def show_tweets():
    return render_template("tweets.html")

@app.route('/register', methods=['GET','POST'])
def register_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        new_user = User.register(username, password)

        db.session.add(new_user)
        db.session.commit()
        flash('Welcome! Successfully Created Your Account! ')
        return redirect('/tweets')

    return render_template('register.html', form=form)


@app.route('/login', methods=["GET","POST"])
def login_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username,password)
        if user:
            return redirect('/tweets')
        else:
            form.username.errors = ['Invalid username/password.']

    return render_template('login.html', form=form)
