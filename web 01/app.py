from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def index():
    
    posts = [
        {
            "title" :"thơ con ếch",
            "content" : "Hôm nay trăng cao quá Anh muốn hôn vào má",
            "author" : "Tuấn Anh",
            "grender":0
        
        },
        {
            "title" : "khô khan",
            "content" : "Hôm nay trăng mới nhú thôi",
            "author" : "Hùng",
            "grender":1
        }
    ]
    
    return render_template("index.html",posts=posts )

@app.route('/hello')

def say_hello():
    return "hello c4e 18"

@app.route("/hi/<name>/<age>")
def hi(name,age):
    return "hi {o}, you are {1} years old ".format(name,age)

@app.route("/sum/<int:x>/<int:y>")
def chia(x,y):
    return str(x + y)

if __name__ == '__main__':
  app.run( debug=True)
 