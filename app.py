# this file is app.py
from helpers import get_products, get_product
from flask import Flask, render_template, request, redirect, url_for
from user import User

app = Flask(__name__)


@app.route("/")
def products():
    return render_template('index.html', products=get_products())


@app.route("/<product_id>")
def product(product_id=None):
    return render_template('product.html', product=get_product(product_id))


@app.route("/sign_up/")
def sign_up():
    return render_template('sign_up.html')


@app.route("/profile/", methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
      user = User(request.form['first_name'], request.form['last_name'], request.form['email'], None, request.form['password'])
      #create a user with the data from the request
      if user.save_to_db():
        return render_template('profile.html')

    return redirect(url_for('sign_up'))
