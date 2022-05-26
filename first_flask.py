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
        conn = mysql.connector.connect(host="127.0.0.1", user="user_one", password="1q2w3e4r", database="Someweres", auth_plugin='mysql_native_password')
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM `clients` where ClientID = '3'""")
        clients = cursor.fetchall()

        firstName = clients[0][1]
        secondName = clients[0][2]
        username = clients[0][3]
        email = clients[0][4]
        phone = clients[0][5]
        sex = clients[0][6]

        cursor.execute("""SELECT ClientID, name FROM `clients` """)
        names = cursor.fetchall()
        pprint.pprint(names)
        client_names=[]
        ''' client_names=[{'id': '1', 'name': 'Vasya'},
                {'id': '2', 'name': 'Petya'},
                {'id': '3', 'name': 'Masha'}
            ]
        '''
        for (name) in names:
            ttt = {'id': name[0], 'name': name[1]}
            pprint.pprint(name)
            print("vasja ttt")
            pprint.pprint(ttt)
            client_names.append(ttt)
        print("vasja CLIENT")
        pprint.pprint(client_names)

        return render_template('bla.html',
            firstName=firstName,
            secondName=secondName,
            username=username,
            email=email,
            phone=phone,
            sex=sex,
            client_names=client_names)

@app.route('/load', methods=['POST'])
def load():

    print("\n\n request object:")
    pprint.pprint(request)

    print("\n\n request form parameter `clientId`:")
    print(request.form['clientId'])

    id_id_id = request.form['clientId']
    bb = request.form['address2']
    message = """sdd----- clientID: {} \n\n\n mbhgbjhgjh \n\n\n adress2: {},
        \n\n\n req:{}""".format(id_id_id, bb, mmm)

    return message
    #render_template('bla.html')

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
