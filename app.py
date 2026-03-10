from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Another year older, another level of awesome. Happy 3rd Birthday NANDHU 3 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# CI/CD test 
