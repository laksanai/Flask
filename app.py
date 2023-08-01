from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/admin')
def member():
    name = "Laksanai" #send value to template
    age = 27
    return render_template("admin.html", myname = name, myAge= age)

if __name__ == "__main__":
    app.run(debug=True)

