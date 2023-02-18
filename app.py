from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/login', methods=['POST','GET'])
def login():
    if(request.method=='POST'):
        phoneNumber = request.form['phoneNumber']
        password = request.form['password']

        # Check if the username and password are correct
        if phoneNumber == '9361598903' and password == 'password':
            return redirect('/crop-list')
        else:
            return render_template('login.html',error="Invalid Credentials")
    else:
        return render_template('login.html')



@app.route('/crop-list')
def croplist():
    return render_template('crop-list.html')


@app.route('/crop-details/chilly')
def chilly():
    return render_template('crop-details/chilly.html')

@app.route('/crop-details/tomato')
def tomato():
    return render_template('crop-details/tomato.html')

@app.route('/crop-details/brinjal')
def brinjal():
    return render_template('crop-details/brinjal.html')

@app.route('/crop-details/snake-gourd')
def snakegourd():
    return render_template('crop-details/snake-gourd.html')
    

if __name__ == '__main__':
    app.run(debug=True)