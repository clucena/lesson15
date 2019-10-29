from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio.html")
def portfolio():
    return render_template("portfolio.html")

@app.route("/about.html")
def about_me():
    return render_template("about.html")

if __name__ == '__main__':
    app.run()