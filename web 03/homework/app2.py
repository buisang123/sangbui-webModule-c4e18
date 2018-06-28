from flask import *
import mlab
from models.service2 import Service
app = Flask(__name__)


mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/route')
def route():
    all_service2 = Service.objects()
    return render_template("route.html",all_service2=all_service2)


@app.route('/details/<service_id>')
def details(service_id):
    service_to_details= Service.objects().get(id=service_id)
    return render_template("details.html",service_to_details=service_to_details)

@app.route('/add',methods=["GET","POST"])
def add():
    if request.method == "GET":  
        return render_template("add.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        height = form["height"]
        phone = form["phone"]
        address = form["address"]
        gender = form["gender"]

        new_service= Service(
            name=name,
            yob=yob,
            height=height,
            phone=phone,
            address=address,
            # gender=gender,
        )
        new_service.save()

        return redirect(url_for('route'))

@app.route('/search')
def search():
    return render_template("search.html")


@app.route('/update/<service_id>', methods=['GET','POST'])
def update(service_id):
    if request.method == 'GET':
        service_up = Service.objects().with_id(service_id)
        return render_template("update.html",service_up=service_up)
    elif request.method == 'POST':
        form = request.form
        service_up = Service.objects().with_id(service_id)
        service_up.update(

            name = form["name"],
            yob = form["yob"],
            address = form["address"]
            

        )
        
        service_up.reload()
        return redirect(url_for("route"))
    

if __name__ == '__main__':
  app.run(debug=True)
 