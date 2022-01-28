from flask import Flask,render_template
import datetime
import spider



app = Flask(__name__)

@app.route('/hdxw')
def hello_world():
    time=datetime.date.today()
    namelist=["zzf","zb","zgl"]#列表传参
    zd = spider.spider()
    return render_template("hdxw.html",var=time,name=namelist,zd=zd)  #var给index.html传参
@app.route('/')
def hdxw():

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
