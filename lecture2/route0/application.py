from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello keats"

@app.route("/david")
def david():
    return "Hello David"



if __name__=="__main__":
    app.run()
