from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1><center>MultiClusterManagement Santander Tecnologia</h1></center>"

if __name__ == "__main__":
    application.run()
