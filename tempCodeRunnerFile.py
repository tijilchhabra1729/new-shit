

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