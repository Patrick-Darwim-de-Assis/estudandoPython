
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.config["DEBUG"] = True

comments = []

@app.route('/', methods = ["POST", "GET"])
def index():
    if request.method == "GET":
        return 'Que a esperança de Deus nunca deixe de estar presente em vós </br><3'+render_template("main_page.html", comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))



