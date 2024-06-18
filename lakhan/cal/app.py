from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("basic.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        expression = request.json.get("expression", "")
        # Evaluate the expression
        result = str(eval(expression))
    except Exception as e:
        result = "Error"
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(debug=True)
