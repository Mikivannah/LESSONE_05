from flask import Flask, render_template

app = Flask(__name__)


@app.route("/shablon/")
def films2():
    context = {

        "link": "Перейти в кинозал"
    }
    return render_template("index.html",  **context)

@app.route("/person/")
def person():
    context = {

        "link": "Перейти в кинозал"
    }

    return render_template("main.html", **context)

if __name__ == "__main__":
    app.run()