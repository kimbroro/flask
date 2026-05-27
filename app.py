from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    print("홈")
    return render_template("index.html")

@app.route("/calcu",methods=['POST'])
def calcu():
    num1=int(request.form["num1"])
    num2=int(request.form["num2"])
    return f"안녕 계산기{num1+num2}"


@app.route("/aa")
def aa():
    print("aa")
    return"aa"

@app.route("/bb")
def bb():
    print("bb")
    return"bb"
if __name__ == "__main__":
    app.run(debug=True)