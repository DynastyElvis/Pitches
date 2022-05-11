import os
import secrets
from flask import abort, render_template, request, url_for, flash, redirect
from pitch import app, db, mail
from pitch.forms import PitchForm, RegistrationForm, LoginForm, UpdateForm, CommentForm, RequestResetForm, ResetPasswordForm
from pitch.models import User, Pitch, Comment
from flask_login import login_user, current_user,login_required, logout_user 
from flask_mail import Message






# Views
@app.route('/', methods=['GET','POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
   
    comments = Comment.query.all()
    pitches = Pitch.query.all()
    user = User.query.all()
    users = list(reversed(user))
    limit = 20
    business = Pitch.query.filter_by(category = 'Business').all()
    finance= Pitch.query.filter_by(category = 'Finance').all()
    relationships= Pitch.query.filter_by(category = 'Relationships').all()
    wellbeing = Pitch.query.filter_by(category = 'Well-Being').all()
    
    return render_template('index.html', pitches = pitches,limit=limit, business=business, finance=finance, relationships=relationships, wellbeing=wellbeing, users=users, comments=comments)

def new_func():
    comments = Comment.query.all()

@app.route('/about')
def about():
    
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form= RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Register', form=form)