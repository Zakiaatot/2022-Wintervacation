from flask import Flask,render_template
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    time=datetime.date.today()
    namelist=["zzf","zb","zgl"]#列表传参
    zd = {"zzf": "19", "zb": "15", "zgl": "62"}
    return render_template("index.html",var=time,name=namelist,zd=zd)  #var给index.html传参
@app.route('/hdxw')
def hdxw():

    return "你好！"
@app.route('/user/<name>')
def welcome(name):

    return "你好!%s"%name

if __name__ == '__main__':
    app.run(debug=True)
