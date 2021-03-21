
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return 'Que a esperança de Deus nunca deixe de estar presente em vós </br><3'+render_template("main_page.html")

