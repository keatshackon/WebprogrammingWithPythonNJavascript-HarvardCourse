from flask  import Flask,render_template
import datetime
app=Flask(__name__)

@app.route("/")
def index():
    new=datetime.datetime.now()
    year=new.day==1 and new.month==1
    year=True
    return render_template("index.html",year=year)


if __name__=="__main__":
    app.run(debug=True)
