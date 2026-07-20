from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "HOME PAGE 🏠"

@app.route("/about")
def about():
    return "About Page"

@app.route("/contact")
def contact():
    return "Contact Page"

print(__name__)

if __name__ == "__main__":
    app.run(debug=True)