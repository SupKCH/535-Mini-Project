from flask import Flask, render_template, request

app = Flask(__name__)
    
ButtonPressed = 0
value = 0
@app.route('/', methods=["GET", "POST"])
def button():
    global ButtonPressed
    if request.method == "POST":
        ButtonPressed += 1
        return render_template("button.html", ButtonPressed = ButtonPressed)
    return render_template("button.html", ButtonPressed = ButtonPressed)

if __name__ == '__main__':
    app.run()
