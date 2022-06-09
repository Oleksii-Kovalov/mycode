def get_client(cursor, clientid):
    print("aaa hui-> \"" + str(clientid) + "\"    hui   hui")
    query = "SELECT * FROM `clients` where ClientID = " + str(clientid)
    print(query)
    return 1

get_client('hui', 3)



def change_client(cursor, conn, firstName, secondName, username, email, phone, sex):
            change = "update clients set Name = " + str(firstName) + ", Surname = " + str(firstName) + ", Username = " + str(firstName) + ", email = " + str(firstName) + ", phone = " + str(firstName) + ", sex = " + str(firstName)" where ClientID = \"" + str(int(clientid)) + "\""
            cursor.execute(change)
            conn.commit()
            pprint.pprint(change)
            return
