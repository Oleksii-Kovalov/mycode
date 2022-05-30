from flask import Flask, render_template
from flask import request
import mysql.connector
import pprint

app = Flask(__name__)


def get_all_clients(cursor):
            cursor.execute("""SELECT ClientID, name FROM `clients` """)
            names = cursor.fetchall()
            pprint.pprint(names)
            client_names=[]

            for (name) in names:
                ttt = {'id': name[0], 'name': name[1]}
                pprint.pprint(name)
                print("vasja ttt")
                pprint.pprint(ttt)
                client_names.append(ttt)
            print("vasja CLIENT")
            pprint.pprint(client_names)

            return client_names

def get_client(cursor, clientid):

    query = "SELECT * FROM `clients` where ClientID = \"" + str(int(clientid)) + "\""
    print(query)
    cursor.execute(query)
    clients = cursor.fetchall()

    (firstName, secondName, username, email, phone, sex) = ('absent', 'absent','absent','absent','absent','absent')

    if len(clients) > 0:
        firstName = clients[0][1]
        secondName = clients[0][2]
        username = clients[0][3]
        email = clients[0][4]
        phone = clients[0][5]
        sex = clients[0][6]

    return firstName, secondName, username, email, phone, sex

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = mysql.connector.connect(host="127.0.0.1", user="user_one", password="1q2w3e4r", database="Someweres", auth_plugin='mysql_native_password')
    cursor = conn.cursor()

    client_names = get_all_clients(cursor)

    if request.method == 'GET':
        (firstName, secondName, username, email, phone, sex) = get_client(cursor, 0)

    if request.method == 'POST':
        id_id_id = request.form['clientId']
        (firstName, secondName, username, email, phone, sex) = get_client(cursor, id_id_id)

    return render_template('bla.html',
            firstName=firstName,
            secondName=secondName,
            username=username,
            email=email,
            phone=phone,
            sex=sex,
            client_names=client_names)


'''
@app.route('/load', methods=['POST'])
def load():
    conn = mysql.connector.connect(host="127.0.0.1", user="user_one", password="1q2w3e4r", database="Someweres", auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    print("\n\n request object:")
    pprint.pprint(request)

    print("\n\n request form parameter `clientId`:")
    print(request.form['clientId'])

    id_id_id = request.form['clientId']
    bb = request.form['address2']

    (firstName, secondName, username, email, phone, sex) = get_client(cursor, id_id_id)
    print( get_client(cursor, id_id_id) )



    message = """sdd----- clientID: {} \n\n\n mbhgbjhgjh \n\n\n adress2: {}""".format(id_id_id, bb)

    return render_template('bla.html',
        firstName=firstName,
        secondName=secondName,
        username=username,
        email=email,
        phone=phone,
        sex=sex,
        client_names = get_all_clients(cursor))
            #render_template('bla.html')
'''

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
