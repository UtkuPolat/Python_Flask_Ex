from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session,
    url_for
)
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

firebaseConfig={
    'apiKey': "AIzaSyCiNDb-MiGfpKL2UEb_tw_dmC_YajH4CTk",
    'authDomain': "akserapp-237aa.firebaseapp.com",
    'databaseURL': "https://akserapp-237aa.firebaseio.com",
    'projectId': "akserapp-237aa",
    'storageBucket': "akserapp-237aa.appspot.com",
    'messagingSenderId': "892016773533",
    'appId': "1:892016773533:web:d1a44d2bd9277c1fd70774",
    'measurementId': "G-VCQ0W4V8SG",
}


firebase = pyrebase.initialize_app(firebaseConfig)

#db = firebase.database()
auth = firebase.auth()
#storage = firebase.storage()

cred = credentials.Certificate('firebase-sdk.json')

app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']

        if auth.sign_in_with_email_and_password(username,password):
            return redirect(url_for('userPage'))
        elif not auth.sign_in_with_email_and_password(username,password):
            return redirect(url_for('login'))


    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/userpage')
def userPage():
    return render_template('userPage.html')

if __name__ == "__main__":
    app.run(debug=True)

