from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def films():
    return render_template("22.html", caption="Фильмы про Гарри")


@app.route("/shablon/")
def films2():
    return render_template("22.html", caption="Гарри Поттор")

@app.route("/person/")
def person():
    return render_template("main.html")

if __name__ == "__main__":
    app.run()