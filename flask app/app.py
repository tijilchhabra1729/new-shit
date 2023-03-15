from hack import app, create_db, db
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from hack.forms import LoginForm, RegForm, SearchForm
from hack.models import User, Sneaker, Size
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid1

create_db(app)

@app.route('/')
def home():
    form = SearchForm()
    sneakers = Sneaker.query.all()
    for i in sneakers:
        i.price = i.price.replace(' ', '').replace(',', '')
        db.session.add(i)
        db.session.commit()
    return render_template('index.html', form=form)

@app.route('/product')
def product():
    form = SearchForm()
    return render_template('product.html', form=form)

@app.route('/search/<query>', methods=['GET', 'POST'])
def search(query):
    shoes = []
    form = SearchForm()
    snkrs = Sneaker.query.order_by(Sneaker.price.asc()).all()
    for i in snkrs:
        if i.name.lower().find(query.lower()) != -1:
            if i.name not in shoes:
                shoes.append(i)
            else:
                print('err')
    return render_template('results.html', shoes=list(dict.fromkeys(shoes)), query=query, form=form)

@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    mess=''
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user:
            mess = 'Account already exists'
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
    return render_template('reg.html', form=form, mess=mess)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    mess=''
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if not user:
            mess = 'Email not found'
        else:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('home'))
            else:
                mess = 'Incorrect password.'
    return render_template('login.html', mess=mess, form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
