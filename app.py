from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_exchange_rates():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    for item in data:
        return item['rates']

@app.route("/", methods=["GET", "POST"])
def currency():
    rates = get_exchange_rates()
    
    if request.method == "POST":
        data = request.form
        code = data.get('code')
        amount = float(data.get("amount"))
        
        for item in rates:
            if code == item['code']:
                return render_template("index.html", amount=amount * item['bid'])
        
    return render_template('index.html', amount=0)

if __name__ == "__main__":
    app.run(debug=True)
