from flask import Flask, render_template, redirect, make_response
from flask import request, jsonify
import mysql.connector
import pprint
import json

app = Flask(__name__)


def get_all_clients(cursor):
            cursor.execute("""SELECT ClientID, name FROM `clients` """)
            names = cursor.fetchall()
            client_names=[]

            for (i) in names:
                ttt = {'id': i[0], 'name': i[1]}
                client_names.append(ttt)
            return client_names

def get_client(cursor, clientid):

    query = "SELECT * FROM `clients` where ClientID = \"" + str(int(clientid)) + "\""
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

def login_required(request):
    loggedin = request.cookies.get('loginsuccessful')
    if loggedin != "Success":
        return redirect('/profile')

@app.route('/', methods=['GET', 'POST'])
def index():
    loggedin = request.cookies.get('loginsuccessful')
    if loggedin != "Success":
        return redirect('/profile')
    conn = mysql.connector.connect(host="127.0.0.1", user="user_one", password="1q2w3e4r", database="Someweres", auth_plugin='mysql_native_password')
    cursor = conn.cursor()

    client_names = get_all_clients(cursor)

    saved = request.cookies.get('saved', '000')

    if request.method == 'GET':
        (firstName, secondName, username, email, phone, sex) = get_client(cursor, 0)

    id_id_id=0
    if request.method == 'POST':
        id_id_id = int(request.form['clientId'])
        (firstName, secondName, username, email, phone, sex) = get_client(cursor, id_id_id)

    templatehui = render_template('bla.html',
            firstName=firstName,
            secondName=secondName,
            username=username,
            email=email,
            phone=phone,
            sex=sex,
            id_id_id=id_id_id,
            saved=saved,
            client_names=client_names)

    response = make_response(templatehui)
    response.delete_cookie('saved')
    cursor.close()
    conn.close()

    return response


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    conn = mysql.connector.connect(host="127.0.0.1", user="user_one", password="1q2w3e4r", database="Someweres", auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    username = request.form.get('Username', 'hui')
    password = request.form.get('Password', 'huilo')

    if username == 'hui':
        action = 'perviy_vhod'
        return render_template('profile.html', action=action)

    admin_data_query = "select Password from `admins` where Username = \"" + username + "\""

    cursor.execute(admin_data_query)
    admindata = cursor.fetchall()
    if len(admindata)==0:
        action = "not correct login"
        return render_template('profile.html', action=action)


    loginseccesful = "None"

    if admindata[0][0] == password:
        loginsuccessful = "Success"


    response = make_response(render_template('profile.html', loginsuccessful = loginsuccessful,))
    response.set_cookie('loginsuccessful', loginsuccessful, max_age=60*60*24*3)
    response.set_cookie('loggedusername', username, max_age=60*60*24*3)
    cursor.close()
    conn.close()

    return response


@app.route('/edituser', methods=['POST'])
# @check_login
def edituser():
    # 1 get cookies loginsuccessfull
    # 2 check if logged in
    # 2.1 success -> run main code
    # 2.2 error -> redirect to login page

    loggedin = request.cookies.get('loginsuccessful')
    if loggedin != "Success":
        return redirect('/profile')
    conn = mysql.connector.connect(host="127.0.0.1", user="user_one", password="1q2w3e4r", database="Someweres", auth_plugin='mysql_native_password')
    cursor = conn.cursor()

    client_names = get_all_clients(cursor)


    firstName = request.form.get('firstName', 'hui')
    secondName = request.form.get('lastName', 'hui')
    username = request.form.get('username', 'hui')
    email = request.form.get('email', 'hui')
    phone = request.form.get('phone', 'hui')
    sex = request.form.get('sex', 'hui')

    clientid = request.form.get('clientId', 'hui')

    change = "update clients set Name = \'" + str(firstName) + "\'" \
        + ", Surname = \'" + str(secondName) + "\'" \
        + ", Username = \'" + str(username) + "\'" \
        + ", email = \'" + str(email) + "\'" \
        + ", phone = \'" + str(phone) + "\'" \
        + ", sex = \'" + str(sex) + "\'" \
        + " where ClientID = \"" + str(int(clientid)) \
        + "\""
    print(change)
    cursor.execute(change)
    conn.commit()

    response = make_response(redirect("/", code=302))
    response.set_cookie('saved', 'true')
    cursor.close()
    conn.close()

    return response

@app.route('/deleteuser', methods=['DELETE'])
def deleteuser():
    loggedin = request.cookies.get('loginsuccessful')
    if loggedin != "Success":
        print("hernja")
        return redirect('/profile')
    conn = mysql.connector.connect(host="127.0.0.1", user="user_one", password="1q2w3e4r", database="Someweres", auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    clientid = request.form.get('clientId', 'hui')
    delete = "delete from clients where ClientID = \"" + str(int(clientid)) \
        + "\""
    print(delete)
    cursor.execute(delete)
    conn.commit()


@app.route('/registration', methods=['GET', 'POST'])
def adduser():
    loggedin = request.cookies.get('loginsuccessful')
    if loggedin != "Success":
        return redirect('/profile')

    conn = mysql.connector.connect(host="127.0.0.1", user="user_one", password="1q2w3e4r", database="Someweres", auth_plugin='mysql_native_password')
    cursor = conn.cursor()

    firstName = request.form.get('firstName', 'hui')
    secondName = request.form.get('lastName', 'hui')
    username = request.form.get('username', 'hui')
    email = request.form.get('email', 'hui')
    phone = request.form.get('phone', 'hui')
    sex = request.form.get('sex', 'hui')


    add = "insert into clients (Name,Surname,Username,email,phone,sex) values (\'" + str(firstName) + "\'" \
        + ",\'" + str(secondName) + "\'" \
        + ",\'" + str(username) + "\'" \
        + ",\'" + str(email) + "\'" \
        + ",\'" + str(phone) + "\'" \
        + ",\'" + str(sex) + "\')" \

    print(add)
    cursor.execute(add)
    conn.commit()

    response = make_response(redirect("/", code=302))
    response.set_cookie('saved', 'true')
    cursor.close()
    conn.close()

    return response


    """
    return render_template('bla.html',
            firstName=firstName,
            secondName=secondName,
            username=username,
            email=email,
            phone=phone,
            sex=sex,
            id_id_id=clientid,
            client_names=client_names)
    """



'''
@app.route('/load', methods=['POST'])id
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


@app.route('/api/clients', methods=['GET'])
def clients():
    conn = mysql.connector.connect(host="127.0.0.1", user="user_one", password="1q2w3e4r", database="Someweres", auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    client_names = get_all_clients(cursor)
    cursor.close()
    conn.close()

    return jsonify(client_names)

@app.route('/api/client', methods=['GET'])
def get_client_api():
    conn = mysql.connector.connect(host="127.0.0.1", user="user_one", password="1q2w3e4r", database="Someweres", auth_plugin='mysql_native_password')
    cursor = conn.cursor()

    clientid = int(request.args.get("id"))
    print(clientid)
    client = get_client(cursor, clientid)
    print(client)
    print(client[0])
    #client = get_client(cursor, id)

    response = make_response(jsonify(client))
    response.status_code=200

    if str(client[0]) == str("absent"):
        response = make_response(jsonify([]))
        response.status_code=404
    cursor.close()
    conn.close()

    return response


@app.route('/api/client', methods=['POST'])
def post_client():
    conn = mysql.connector.connect(host="127.0.0.1", user="user_one", password="1q2w3e4r", database="Someweres", auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    if request.args.get("id") == None:
        response = make_response(jsonify("Missing requered parameter: id"))
        response.status_code=412
        cursor.close()
        conn.close()
        return response

    clientid = int(request.args.get("id"))

    (firstName, secondName, username, email, phone, sex) = get_client(cursor, clientid)

    if firstName == "absent":
        response = make_response(jsonify("Client not found"))
        response.status_code=404
        cursor.close()
        conn.close()
        return response

    firstName = request.form.get('firstName', 'hui')
    secondName = request.form.get('lastName', 'hui')
    username = request.form.get('username', 'hui')
    email = request.form.get('email', 'hui')
    phone = request.form.get('phone', 'hui')
    sex = request.form.get('sex', 'hui')


    change = "update clients set Name = \'" + str(firstName) + "\'" \
        + ", Surname = \'" + str(secondName) + "\'" \
        + ", Username = \'" + str(username) + "\'" \
        + ", email = \'" + str(email) + "\'" \
        + ", phone = \'" + str(phone) + "\'" \
        + ", sex = \'" + str(sex) + "\'" \
        + " where ClientID = \"" + str(int(clientid)) \
        + "\""
    print(change)
    cursor.execute(change)
    conn.commit()

    response = make_response("saved seccesful")
    response.status_code=200

    cursor.close()
    conn.close()

    return response


@app.route('/api/client', methods=['PUT'])
def put_client(): # put=create
    conn = mysql.connector.connect(host="127.0.0.1", user="user_one", password="1q2w3e4r", database="Someweres", auth_plugin='mysql_native_password')
    cursor = conn.cursor()

    firstName = request.form.get('firstName', 'hui')
    secondName = request.form.get('lastName', 'hui')
    username = request.form.get('username', 'hui')
    email = request.form.get('email', 'hui')
    phone = request.form.get('phone', 'hui')
    sex = request.form.get('sex', 'hui')

    change = "insert into clients set Name = \'" + str(firstName) + "\'" \
        + ", Surname = \'" + str(secondName) + "\'" \
        + ", Username = \'" + str(username) + "\'" \
        + ", email = \'" + str(email) + "\'" \
        + ", phone = \'" + str(phone) + "\'" \
        + ", sex = \'" + str(sex) + "\'"

    print(change)
    cursor.execute(change)
    conn.commit()

    response = make_response("saved seccesful")
    response.status_code=200

    cursor.close()
    conn.close()

    return response


@app.route('/api/client', methods=['DELETE'])
def delete_client():
    conn = mysql.connector.connect(host="127.0.0.1", user="user_one", password="1q2w3e4r", database="Someweres", auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    if request.args.get("id") == None:
        response = make_response(jsonify("Missing requered parameter: id"))
        response.status_code=412
        cursor.close()
        conn.close()
        return response

    clientid = int(request.args.get("id"))

    (firstName, secondName, username, email, phone, sex) = get_client(cursor, clientid)
    if firstName == "absent":
        response = make_response(jsonify("Client not found"))
        response.status_code=404
        cursor.close()
        conn.close()
        return response

    delete = "delete from clients where ClientID = \"" + str(int(clientid)) \
        + "\""
    print(delete)
    cursor.execute(delete)
    conn.commit()

    response = make_response("delete seccesful")
    response.status_code=200

    cursor.close()
    conn.close()

    return response


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
