#from flask import Flask
from flask import Flask, redirect, render_template, request, url_for

application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1><center>MultiClusterManagement Santander Tecnologia</h1></center>"

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/login/", methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        return redirect(url_for('user', username=username))
    return redirect(url_for('index'))

@app.route("/user/")
@app.route("/user/<username>")
def user(username=None):
    if not username:
        return redirect(url_for('index'))
    return render_template('user.html', username=username)    

if __name__ == "__main__":
    application.run()
