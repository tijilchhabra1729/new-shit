import dump
import requests
from bs4 import BeautifulSoup as bs
import validators
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

db = SQLAlchemy()
app = Flask(__name__)
db_name = 'sneaker_db.sqlite'
app.config['SECRET_KEY'] = "helloworld"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
db.init_app(app)
titles = []
prices = []
sizes = []

class Sneaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.String)
    img = db.Column(db.String)
    url = db.Column(db.String)
    sizes = db.relationship('Size', backref='snkr')
    
class Size(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String)
    sneaker = db.Column(db.Integer, db.ForeignKey('sneaker.id'))
    
app.app_context().push()
db.create_all()

headers = {
    'User-Agent': 'Mozilla/5.0'
}

# for i in dump.veg_non_veg:
#     try:
#         req = requests.get(i, headers=headers)
#         vnv = bs(req.content, 'lxml')
#         print(vnv.find('h1').text)
#     except Exception as e:
#        print(i, e)

# for i in list(dict.fromkeys(dump.superkicks)):
#     try:
#         req = requests.get(i, headers=headers)
#         sk = bs(req.content, 'lxml')
#         sizes = sk.find_all('label', class_='OutOfStock') + sk.find_all('label', class_='InStock')
#         img = sk.find('div', class_='product__media media media--transparent gradient global-media-settings').find('img').get('src')
#         size = [x.text.strip() for x in sizes]
#         new_snkr = Sneaker(name=sk.find('title').text.strip().replace('\n', ''),url=i,img=img, price=sk.find('span', class_='price-item price-item--regular').text.strip().replace('\n', ''))
#         new_size = ''
#         for k in sizes:
#             new_size = Size(size=k.text.strip(), sneaker=new_snkr.id)
#             new_snkr.sizes.append(new_size)
#             db.session.add(new_snkr)
#         db.session.commit()
#     except Exception as e:
#         print(i, e)
        
# for i in list(dict.fromkeys(dump.dawntown)):
#     try:
#         req = requests.get(i, headers=headers)
#         sk = bs(req.content, 'lxml')
#         img = sk.find('div', class_='product__media media media--transparent media__height').find('img').get('src')
#         new_snkr = Sneaker(name=sk.find('title').text.strip().replace('\n', ''),url=i, price=sk.find('span', class_='price-item price-item--regular').text.strip().replace('\n', ''), img=img)
#         new_size = ''
#         sizes = size=sk.find('variant-radios').find_all('label')
#         for j in sizes:
#             new_size  = Size(size=j.text.strip(), sneaker=new_snkr.id)
#             new_snkr.sizes.append(new_size)
#             db.session.add(new_size)
#         db.session.add(new_snkr)
#         db.session.commit()
#     except Exception as e:
#         print(i, e)
        
# for i in list(dict.fromkeys(dump.crepdog)):
#     try:
#         req = requests.get(i, headers=headers)
#         sk = bs(req.content, 'lxml')
#         img = sk.find('img', class_='Image--fadeIn lazyautosizes Image--lazyLoaded')
#         new_snkr = Sneaker(name=sk.find('h1', class_='ProductMeta__Title Heading u-h2').text.strip().replace('\n', ''),url=i, price=sk.find('span', class_='money').text.strip().replace('\n', ''), img=img)
#         new_size = ''
#         sizes = sk.find('div', class_='Popover__ValueList').find_all('button')
#         for j in sizes:
#             new_size  = Size(size=j.text.strip(), sneaker=new_snkr.id)
#             new_snkr.sizes.append(new_size)
#             db.session.add(new_size)
#         db.session.add(new_snkr)
#         db.session.commit()
#     except Exception as e:
#         print(i, e)

for i in list(dict.fromkeys(dump.mainstreet)):
        k = 'https://marketplace.mainstreet.co.in/' + i
    # try:
        req = requests.get(k, headers=headers)
        sk = bs(req.content, 'lxml')
        print(sk.find('h1', class_='product-single__title').text.strip().replace('\n', ''))
        # new_snkr = Sneaker(name=sk.find('h1', class_='product-single__title').text.strip().replace('\n', ''),url=k, price=sk.find('span', class_='product-single__price').text.strip().replace('\n', ''))
        # new_size = ''
        # sizes = sk.find('select', class_='single-option-selector').find_all('option')
        # for j in sizes:
        #     new_size  = Size(size=j.text.strip(), sneaker=new_snkr.id)
        #     new_snkr.sizes.append(new_size)
        #     db.session.add(new_size)
        # db.session.add(new_snkr)
        # db.session.commit()
    # except Exception as e:
    #     print(i, e)

# for i in list(dict.fromkeys(dump.mainstreet)):
#     k = 'https://marketplace.mainstreet.co.in/' + i
#     try:
#         req = requests.get(k, headers=headers)
#         sk = bs(req.content, 'lxml')
#         print(sk.find('h1', class_='product-single__title'))
#         print(sk.find('h1', class_='product-single__title'))
#         # new_snkr = sk.find('h1', class_='product-single__title').text.strip().replace('\n', '')
#         # snkrs = Sneaker.query.filter(Sneaker.name.like('%' + new_snkr + '%')).all()
#         # print(snkrs)
#     except Exception as e:
#         print(i, e)



# for i in list(dict.fromkeys(dump.crepdog)):
#     try:
#         req = requests.get(i, headers=headers)
#         cd = bs(req.content, 'lxml')
#         snkr = Sneaker.query.filter_by(name=cd.find('h1', class_='ProductMeta__Title Heading u-h2').text.strip().replace('\n', '')).first()
#         img = cd.find('div', class_='Product__SlideItem Product__SlideItem--image Carousel__Cell is-selected').find('img').get('data-src').replace('{width}', '1400')
#         snkr.img = img
#         db.session.add(snkr)
#         db.session.commit()
#     except Exception as e:
#         print(e)



class SearchForm(FlaskForm):
    query = StringField()
    submit = SubmitField('Search')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    snkr = Sneaker.query
    if form.validate_on_submit():
        snkr = snkr.filter(Sneaker.name.like('%' + form.query.data + '%'))
        snkr = snkr.order_by(Sneaker.price.asc()).all()
    return render_template('index.html', form=form, snkr=snkr)

if __name__ == '__main__':
    app.run(debug=True)