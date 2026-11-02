from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python Jenkins Pipeline</title>
    </head>
    <body>
        <h1>PYTHON PIPELINE PROJECT</h1>
        <h2>Jenkins Build Successful</h2>
        <p>This website is deployed using Jenkins Pipeline.</p>
        <p>GitHub → Jenkins → Build → Test → Deploy</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
