from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello,Keats Salazar"


@app.route("/<string:name>")
def anyname(name):
    name=name.capitalize()
    return f"Hello {name}"

if __name__=="__main__":
    app.run()
