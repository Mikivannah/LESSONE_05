from flask import Flask, render_template

app = Flask(__name__)


@app.route("/shablon/")
def films2():
    context = {
        "caption": "Гарри Поттер",
        "link": "Перейти в кинозал"
    }
    return render_template("index.html",  **context)

@app.route("/person/")
def person():
    return render_template("main.html")

if __name__ == "__main__":
    app.run()