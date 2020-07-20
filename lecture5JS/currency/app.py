from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    currency = request.form.get("currency")
    res = request.get("https://currencyconv.p.rapidapi.com/currency_conversion", params={
        "base": "USD", "symbols": currency})


    if res.status_code !=200:
        return jsonify({"success":False})

    data = res.json()
    if(currency not in data["rates"]):
        return jsonify({"success":False})

    return jsonify({"success":True,"rate":data["rates"][currency]})




if __name__ == "__main__":
    app.run(debug = True)
