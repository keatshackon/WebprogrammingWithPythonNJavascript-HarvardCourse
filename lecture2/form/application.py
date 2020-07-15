from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello",methods=["POST","GET"])
def hello():
    if(request.method == "GET"):
        return "Please Fill The Form!"
    else:
        name=request.form.get("name")
        return render_template("hello.html",name=name)

if __name__=="__main__":
    app.run(debug=True)
