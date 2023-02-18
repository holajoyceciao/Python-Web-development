from flask import Flask, render_template, request, redirect
import csv
import env

app = Flask(__name__, static_folder='../frontend/static', template_folder = '../frontend')

@app.route('/index')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name + '.html')

# @app.route('/about')
# def my_about():
#     return render_template('about.html')

# @app.route('/works')
# def my_works():
#     return render_template('works.html')

# @app.route('/work')
# def my_work():
#     return render_template('work.html')
    
# @app.route('/contact')
# def contact_me():
#     return render_template('contact.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try: 
            data = request.form.to_dict() # convert the data to dictionary
            write_to_csv(data)
            return redirect('/thankyou')
        except:
            return 'data did not save to the database.'
    else:
        return 'something went wrong. Try again.'

# This code replaced 'flask run' command line. It will be run when you apply 'python YOUR_PYTHON_FILE_NAME'
if __name__ == '__main__': 
    app.run(host = env.HOST, port = env.PORT, debug = env.DEBUG_MODE) 