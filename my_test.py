def get_client(cursor, clientid):
    print("aaa hui-> \"" + str(clientid) + "\"    hui   hui")
    query = "SELECT * FROM `clients` where ClientID = " + str(clientid)
    print(query)
    return 1

get_client('hui', 3)



if request.method == 'POST':

    pprint.pprint(request.form['firstName'])
    pprint.pprint(request.form['lastName'])
    pprint.pprint(request.form['username'])
    pprint.pprint(request.form['email'])
    pprint.pprint(request.form['Phonenumber'])

    pprint.pprint(request.form)
