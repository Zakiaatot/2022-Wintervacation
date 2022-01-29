from flask import Flask,render_template
import datetime
import spider



app = Flask(__name__)

# / 的访问通过nginx静态代理实现，不用flask

@app.route('/hdxw')
def hello_world():
    time=datetime.date.today()

    zd = spider.spider()
    return render_template("hdxw.html",var=time,zd=zd)  #var给index.html传参



if __name__ == '__main__':
    app.run(debug=True)
