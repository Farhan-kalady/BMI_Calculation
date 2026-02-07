from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])

        bmi = weight / (height * height)

        return render_template("result.html", bmi=round(bmi, 2))
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
