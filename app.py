from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 's8 project'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST','GET'])
def signup():
    if(request.method=='POST'):
        name = request.form['name']
        number = request.form['number']
        password = request.form['password']
        address = request.form['address']
        district = request.form['district']

        cursor = mysql.connection.cursor()
        cursor.execute("Insert into user values(%s,%s ,%s, %s, %s)", (name, number, password, address, district))
        mysql.connection.commit()
        cursor.close()
        return redirect('/login')
    else:
        return render_template('signup.html')


@app.route('/login', methods=['POST','GET'])
def login():
    if(request.method=='POST'):
        phoneNumber = request.form['phoneNumber']
        password = request.form['password']
        
        cursor = mysql.connection.cursor()
        cursor.execute("Select * from user where phone=%s and password=%s", (phoneNumber, password))
        account = cursor.fetchone()


        if account:
            return redirect('/addProduct')
            
        else:
            return render_template('login.html',error="Invalid Credentials")
    else:
        return render_template('login.html')

@app.route('/crop-list')
def croplist():
    return render_template('crop-list.html')

@app.route('/addProduct')
def addProcut():
    return render_template('addProduct.html')


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
    
@app.route('/crop-details/bhendi')
def bhendi():
    return render_template('crop-details/bhendi.html')

@app.route('/crop-details/bitter-gourd')
def bittergourd():
    return render_template('crop-details/bitter-gourd.html')

@app.route('/crop-details/bottle-gourd')
def bottlegourd():
    return render_template('crop-details/bottle-gourd.html')

@app.route('/crop-details/ash-gourd')
def ashgourd():
    return render_template('crop-details/ashgourd.html')

@app.route('/crop-details/potato')
def potato():
    return render_template('crop-details/potato.html')
    
@app.route('/crop-details/ribbed-gourd')
def ribbedgourd():
    return render_template('crop-details/ribbed-gourd.html')

if __name__ == '__main__':
    app.run(debug=True)