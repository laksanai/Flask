from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    data = {"name": "laksaanai", "age":27, "salary":15000}
    return render_template("index.html", myData = data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/admin')
def profile():
    name = "Laksanai" #send value to template
    age = 27
    return render_template("admin.html", myname = name, myAge= age)

if __name__ == "__main__":
    app.run(debug=True)

