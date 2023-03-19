from flask import Flask

app = Flask(__name__)

@app.route("/")
def sen():
    return "It's better to burn out than to fade away."

if __name__ == "__main__":
    app.run(port=8000)
