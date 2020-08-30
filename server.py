from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)
import csv

@app.route('/')
def home():
    return render_template('index.html')

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         database.write(f'\nemail: {email} - subject: {subject} - message: {message}')

def write_to_csv(data):
    with open('DB.csv', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL )
        csv_writer.writerow([email, subject, message])


@app.route('/<string:pagename>')
def works(pagename):
    return render_template(pagename) 

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/regards.html')
    else:
        return 'Something is wrong! :('