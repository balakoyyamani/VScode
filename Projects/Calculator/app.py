from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""

    if request.method == "POST":
        try:
            n1 = float(request.form["num1"])
            n2 = float(request.form["num2"])
            op = request.form["operator"]

            match op:
                case "+":
                    result = n1 + n2
                case "-":
                    result = n1 - n2
                case "*":
                    result = n1 * n2
                case "/":
                    if n2 == 0:
                        result = "Cannot divide by zero"
                    else:
                        result = n1 / n2
                case "%":
                    if n2 == 0:
                        result = "Cannot divide by zero"
                    else:
                        result = n1 % n2
                case "**":
                    result = n1 ** n2
                case _:
                    result = "Invalid Operator"

        except:
            result = "Invalid Input"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)