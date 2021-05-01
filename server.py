from flask import Flask,render_template,request,redirect
import csv
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form',methods=["POST"])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "Did not save to the database."
    else:
        return 'Something went wrong.Please try again.'

def write_to_file(data):
    with open("database.txt",mode='a') as database_file:
        database_file.write(f"\n{data['email']},{data['subject']},{data['message']}")

def write_to_csv(data):
    with open("database2.csv",newline='',mode='a') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data['email'],data['subject'],data['message']])