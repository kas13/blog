from app_dir import app
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from app_dir.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", name='wqeq')

@app.route("/members")
def members():
    return "Members"


@app.route("/members/<string:name>/")
def get_mebmer(name):
    return render_template("index.html", name=name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
