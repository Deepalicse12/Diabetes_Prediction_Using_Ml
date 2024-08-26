from flask import Flask, redirect, request, render_template, flash, url_for

import pickle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'

scaler = pickle.load(open('scaler.pkl', 'rb'))
model = pickle.load(open('svm_model.pkl', 'rb'))

@app.route('/')
def new():
    return render_template('home.html')

@app.route('/home.html')
def few():
    return render_template('home.html')

@app.route('/history.html')
def user():
    return render_template('history.html')

@app.route('/health_tips.html')
def user3():
    return render_template('health_tips.html')

@app.route('/Predict')
def prediction():
    return render_template('login.html')
    

USERNAME = 'admin'
PASSWORD = 'admin'

@app.route('/')
def house():
    return render_template('login.html')

@app.route('/login.html', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == USERNAME and password == PASSWORD:
        flash('Login successful!', 'success')
        return redirect(url_for('/index'))  # Redirect to index route upon successful login
    else:
        flash('Invalid credentials. Please try again.', 'danger')
        return redirect(url_for('/home.html'))

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = -1
    if request.method == 'POST':
        pregs = int(request.form.get('pregs'))
        gluc = int(request.form.get('gluc'))
        bp = int(request.form.get('bp'))
        skin = int(request.form.get('skin'))
        insulin = float(request.form.get('insulin'))
        bmi = float(request.form.get('bmi'))
        func = float(request.form.get('func'))
        age = int(request.form.get('age'))

        input_features = [[pregs, gluc, bp, skin, insulin, bmi, func, age]]
        # print(input_features)
        prediction = model.predict(scaler.transform(input_features))
        # print(prediction)
        
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)