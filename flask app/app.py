from hack import app, create_db, db, get_google_provider_cfg, client, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET
from flask import render_template, redirect, url_for, flash, session, request, abort
from flask_login import current_user, login_user, logout_user, login_required
from hack.forms import LoginForm, RegForm, SearchForm
from hack.models import User, Sneaker, Size
from werkzeug.security import generate_password_hash, check_password_hash
from oauthlib.oauth2 import WebApplicationClient
import google.auth.transport.requests
from pip._vendor import cachecontrol
import requests
from urllib.parse import unquote
import json
from uuid import uuid4

create_db(app)

@app.route('/')
def home():
    form = SearchForm()  #the final page where the authorized users will end up
    # sneakers = Sneaker.query.all()
    # for i in sneakers:
    #     i.price = i.price.replace(' ', '').replace(',', '')
    #     db.session.add(i)
    #     db.session.commit()
    # sneakers = Sneaker.query.all()
    # sneakers = [*set(sneakers)]
    # db.session.add(sneakers)
    # db.session.commit()
    # shoes = []
    # sneakers = Sneaker.query.all()
    # # for i in sneakers:
    # #     if i not in shoes:
    # #         shoes.append(i)
    # # print(len(shoes))
    # sk = sneakers[:447]
    # dup_names = []
    # for i in sk:
    # #     print(len(list(dict.fromkeys(sk))))
    # unique_sneakers = []
    # sneakers = Sneaker.query.all()
    # for i in sneakers:
    #     if i.name not in unique_sneakers:
    #         unique_sneakers.append(i.name)
    #     else:
    #         sneaker = Sneaker.query.filter_by(name=i.name).first()
    #         db.session.delete(sneaker)
    #         db.session.commit()
    return render_template('dist/index.html', form=form)

@app.route('/products/<id>')
def product(id):
    form = SearchForm()
    product = Sneaker.query.filter_by(id=id).first()
    return render_template('product.html', form=form, product=product)

@app.route('/search', methods=['GET', 'POST'])
def search_main():
    form = SearchForm()
    return render_template('dist/search.html', form=form)

@app.route('/sendsearch', methods=['GET', 'POST'])
def send_search():
    form = SearchForm()
    return redirect(url_for('search', query=form.query.data))

@app.route('/signinwithgoogle', methods=['GET', 'POST'])
def sign_in_with_google():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@app.route('/signinwithgoogle/callback', methods=['GET', 'POST'])
def sign_in_with_google_callback():
    code = request.args.get("code")
    # Find out what URL to hit to get tokens that allow you to ask for
# things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
    token_endpoint,
    authorization_response=request.url,
    redirect_url=request.base_url,
    code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )
    client.parse_request_body_response(json.dumps(token_response.json()))
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
        email_chk = User.query.filter_by(email=users_email).first()
        if email_chk:
            login_user(email_chk, remember=True)
            return redirect(url_for('home'))
        else:
            new_user = User(email=users_email, username=users_name, password=generate_password_hash(str(uuid4())))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('home'))
    else:
        return "User email not available or not verified by Google.", 400




@app.route('/search/<query>', methods=['GET', 'POST'])
def search(query):
    shoes = []
    form = SearchForm()
    snkrs = Sneaker.query.order_by(Sneaker.price.asc()).all()
    for i in snkrs:
        if i.name.lower().replace('&', 'and').replace(' n ', 'and').find(query.lower().replace('&', 'and').replace(' n ', ' and ')) != -1:
            if i not in shoes:
                shoes.append(i)
            else:
                print('err')
    return render_template('dist/results.html', shoes=shoes, query=query, form=form)
        

@app.route('/signup', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    mess=''
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        email_chk = User.query.filter_by(email=email).first()
        username_chk = User.query.filter_by(username=email).first()
        if email_chk or username_chk:
            mess = 'An account already exists with this email and/or username.'
        else:  
            new_user = User(email=email, username=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('home'))
    return render_template('dist/register.html', form=form, mess=mess)

@app.route('/signin', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    mess=''
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        email_chk = User.query.filter_by(email=email).first()
        username_chk = User.query.filter_by(username=email).first()
        if email_chk:
            if check_password_hash(email_chk.password, password):
                login_user(email_chk, remember=True)
                return redirect(url_for('home'))
            else:
                mess = 'Incorrect password.'
    return render_template('dist/login.html', mess=mess, form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
