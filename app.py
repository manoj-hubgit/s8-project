from flask import Flask, render_template, request, redirect,make_response
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

        if(district=='erode' or district=='Erode' or district=='erd'):
            cursor = mysql.connection.cursor()
            cursor.execute("Insert into user(name,phone_num,password,address,district) values(%s,%s ,%s, %s, %s)", (name, number, password, address, district))
            mysql.connection.commit()
            cursor.close()
            return redirect('/login')
        else:
            return render_template('signup.html',error="Only available for Erode")
    else:
        return render_template('signup.html')


@app.route('/login', methods=['POST','GET'])
def login():
    if(request.method=='POST'):
        phoneNumber = request.form['phoneNumber']
        password = request.form['password']
        
        cursor = mysql.connection.cursor()
        cursor.execute("Select * from user where phone_num=%s and password=%s", (phoneNumber, password))
        account = cursor.fetchone()


        if account:
            response = make_response(redirect('/addProduct'))
            response.set_cookie('userId', str(account[0]))
            
            return response
           
            
        else:
            return render_template('login.html',error="Invalid Credentials")
    else:
        return render_template('login.html')

@app.route('/products',methods=['POST','GET'])
def products():
    if(request.method=='POST'):
        print(request.data)
        productType=request.form['productType'].lower()
        productName=request.form['productName'].lower()
        quantity=request.form['quantity'].lower()
        quantityType=request.form['quantityType'].lower()
        userId=request.form['userId']
        cursor = mysql.connection.cursor()
        cursor.execute("Insert into products(product_type,product_name,quantity,quantity_type,user_id) values(%s,%s ,%s, %s, %s)", (productType, productName, quantity, quantityType, userId))
        mysql.connection.commit()
        cursor.close()
        
        return "success"
    else:
        args = request.args.to_dict()
        userId=args.get('userId')
        cursor = mysql.connection.cursor()
        cursor.execute("Select * from products where product_type='machinary'")
        data = cursor.fetchall()
        print(str(cursor))

        addcursor = mysql.connection.cursor()
        addcursor.execute("Select address,phone_num,user_id,name from user")
        addData = addcursor.fetchall()
        print(str(addcursor))

        
        result={"data":data}

        for i in range(len(addData)):
            result[str(addData[i][2])] = addData[i]

        print(result)

        
        return result

@app.route('/seeds',methods=['POST','GET'])
def seeds():
    if(request.method=='POST'):
        print(request.data)
        productType=request.form['productType'].lower()
        productName=request.form['productName'].lower()
        quantity=request.form['quantity'].lower()
        quantityType=request.form['quantityType'].lower()
        userId=request.form['userId']
        cursor = mysql.connection.cursor()
        cursor.execute("Insert into products(product_type,product_name,quantity,quantity_type,user_id) values(%s,%s ,%s, %s, %s)", (productType, productName, quantity, quantityType, userId))
        mysql.connection.commit()
        cursor.close()
        
        return "success"
    else:
        args = request.args.to_dict()
        userId=args.get('userId')
        cursor = mysql.connection.cursor()
        cursor.execute("Select * from products where product_type='seeds' or product_type='fertilizer'")
        data = cursor.fetchall()
        print(str(cursor))
        
        addcursor = mysql.connection.cursor()
        addcursor.execute("Select address,phone_num,user_id,name from user")
        addData = addcursor.fetchall()
        print(str(addcursor))

        
        result={"data":data}

        for i in range(len(addData)):
            result[str(addData[i][2])] = addData[i]

        print(result)

        return result
    
@app.route('/fertilizers',methods=['POST','GET'])
def fertilizers():
        args = request.args.to_dict()
        userId=args.get('userId')
        cursor = mysql.connection.cursor()
        cursor.execute("Select * from products where product_type='fertilizer'")
        data = cursor.fetchall()
        print(str(cursor))

        addcursor = mysql.connection.cursor()
        addcursor.execute("Select address,phone_num,user_id,name from user")
        addData = addcursor.fetchall()
        print(str(addcursor))

        
        result={"data":data}

        for i in range(len(addData)):
            result[str(addData[i][2])] = addData[i]

        print(result)

        return result
    
@app.route('/crop-list')
def croplist():
    return render_template('crop-list.html')

@app.route('/viewProducts')
def viewProducts():
    return render_template('products.html')

@app.route('/viewFertilizers')
def viewFertilizers():
    return render_template('fertilizers.html')

@app.route('/viewSeeds')
def viewSeeds():
    return render_template('seeds.html')

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
    return render_template('crop-details/ash-gourd.html')

@app.route('/crop-details/potato')
def potato():
    return render_template('crop-details/potato.html')
    
@app.route('/crop-details/ribbed-gourd')
def ribbedgourd():
    return render_template('crop-details/ribbed-gourd.html')

if __name__ == '__main__':
    app.run(debug=True)