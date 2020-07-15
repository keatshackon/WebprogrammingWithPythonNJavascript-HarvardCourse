from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    head="Hello Universe"
    return render_template("index.html",head=head)


if __name__=="__main__":
    app.run(debug=True)
