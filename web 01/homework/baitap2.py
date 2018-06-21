from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<kg>/<m>')

def index(kg,m):
    
    BMI = str(float(kg)/(float(m)*float(m)))
    if BMI <= str(int(16)):
        return"thieu can nang"
    elif BMI <= str(int(18.5)):
        return"thieu can"
    elif BMI <= str(int(25)):
        return"binh thuong"
    elif BMI <= str(int(30)):
        return"thua can"
    else:
        return"beo phi"


if __name__ == '__main__':
  app.run( debug=True)
 