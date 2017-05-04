from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from random import randrange

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    return render_template('index.html',
                           title='Home',
                           user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@app.route('/liow', methods=['GET', 'POST'])
def liow():
    form = LoginForm()

    if form.validate_on_submit():
        return ('%s, %d' %(form.openid.data, randrange(0,20)))
        
    return render_template('input.html',
                           title='Liow stuff',
                           form=form)
