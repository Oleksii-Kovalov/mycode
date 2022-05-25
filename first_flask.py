from flask import Flask, render_template
from flask import request
import mysql.connector
import pprint

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():


    if request.method == 'POST':

        pprint.pprint(request.form['firstName'])
        pprint.pprint(request.form['lastName'])
        pprint.pprint(request.form['username'])
        pprint.pprint(request.form['email'])
        pprint.pprint(request.form['Phonenumber'])

        pprint.pprint(request.form)

        #mysql code here

    if request.method == 'GET':
        print("1")
        conn = mysql.connector.connect(host="127.0.0.1", user="user_one", password="1q2w3e4r", database="Someweres", auth_plugin='mysql_native_password')
        print("2")
        cursor = conn.cursor()
        print("3")
        cursor.execute("""SELECT * FROM `clients` where ClientID = '4'""")
        print("4")
        clients = cursor.fetchall()
        pprint.pprint(clients)


        firstName=clients[0][1]
        secondName = clients[0][2]
        username = clients[0][3]
        email = clients[0][4]
        phone = clients[0][5]
        sex = clients[0][6]
        
    return render_template('bla.html', firstName=firstName, secondName=secondName, username=username, email=email, phone=phone, sex=sex)



@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/registration', methods=['GET'])
def registration():
    return render_template('registration.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run()
