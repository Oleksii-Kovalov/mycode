from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        import pprint
        pprint.pprint(request.form['firstName'])
        pprint.pprint(request.form['lastName'])
        pprint.pprint(request.form['username'])
        pprint.pprint(request.form['email'])
        pprint.pprint(request.form['Phonenumber'])

        pprint.pprint(request.form)

        #mysql code here
        
    return render_template('bla.html')



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
