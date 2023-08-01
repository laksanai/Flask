from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello Flask framework</h1>"

@app.route('/user/<name>') #Here dinymic route
def menber(name):
    return "<h1>สวัสดีสมาชิก: {}</h1>".format(name[1000])

if __name__ == "__main__":
    app.run(debug=True)

