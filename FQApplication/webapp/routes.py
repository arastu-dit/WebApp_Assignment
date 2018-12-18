from flask import render_template, url_for, flash, redirect
from webapp import app
from webapp.forms import RegistrationForm, LoginForm
from webapp.models import User, Post

posts = [

    {
        'event_organizer': 'Arastu Kumar',
        'event_name': 'Football Tournament',
        'event_venue': 'Jawarlal Nehru Stadium',
        'date_posted': '15th December 2018'
    },

    {
        'event_organizer': 'Tanishq Sharma',
        'event_name': 'Cricket Tournament',
        'event_venue': 'Ambedkar Stadium',
        'date_posted': '16th December 2018'
    },
    {
        'event_organizer': 'Dhruv Razdan',
        'event_name': 'Trekking',
        'event_venue': 'Ladakh',
        'date_posted': '18th December 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@fq.com' and form.password.data == 'admin':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your credentials', 'danger')
    return render_template('login.html', title='Login', form=form)