import os

from flask import Flask, render_template, request
from dotenv import load_dotenv

from login_form import LoginForm

load_dotenv()

app = Flask(__name__)

app.secret_key = os.environ['WTF_CSRF_SECRET_KEY']


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == 'admin@email.com' and password == '12345678':
            return render_template('success.html', form=form)
        else:
            return render_template('denied.html', form=form)

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
