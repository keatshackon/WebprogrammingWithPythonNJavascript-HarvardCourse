from flask import Flask ,request ,render_template,session
from flask_session import Session

app=Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/", methods=["GET","POSt"])
def index():
    if(session.get("notes") is None):
        session["notes"] = []
    if(request.method == "POST" and request.form.get("note")!=""):
        note = request.form.get("note")
        session["notes"].append(note)
        notes.append(note)
    return render_template("index.html",notes=session["notes"])

if __name__=="__main__":
    app.run(debug=True)
