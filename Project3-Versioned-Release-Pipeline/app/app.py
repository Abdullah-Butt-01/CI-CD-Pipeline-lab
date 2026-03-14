from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Versioned CI/CD Pipeline Running 🚀 tag 1.2, Checking if paths in the workflow dont not cause problem again"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
