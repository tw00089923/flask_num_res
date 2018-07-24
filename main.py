from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<int:first>/<int:second>')
def project(first, second):
    return " 數字相乘 {}".format( first*second )

@app.route('/<first>/<second>')
def wrong_page(first, second):
    return render_template('bad.html',first = first, second = second )

if __name__ == "__main__":
    app.run(debug=False)