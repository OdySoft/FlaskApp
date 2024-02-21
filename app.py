from flask import Flask , render_template , url_for , request
from src.data import data

app = Flask(__name__)

@app.route("/")
def home():
    print(request.endpoint)
    return render_template("index.html")

@app.route("/shop")
def shop():
    return render_template('shop.html' , products = data)

@app.route("/product/<int:product_id>")
def product(product_id):
    return render_template("product.html", product = data[product_id])

if __name__ == "__main__":
    app.run(debug=True)