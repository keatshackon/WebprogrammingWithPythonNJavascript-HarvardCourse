from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    l=["Keats","Salazar","Sineboi","Scientist","hackon"]
    return render_template("index.html",name=l)


if __name__=="__main__":
    app.run(debug=True)
