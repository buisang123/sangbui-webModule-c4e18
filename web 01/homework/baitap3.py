from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def index(username):
   
    if username == "quý":
        return render_template("quy.html")
    elif username == "tuananh":
        return render_template("tuananh.html")
    else:
        return "User not found"
if __name__ == '__main__':
  app.run(debug=True)
 