from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Test git hub action!"


if __name__ == "__main__":
    app.run()
