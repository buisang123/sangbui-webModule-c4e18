from flask import *
import mlab
from models.service import Service
from models.customer import Customer


app = Flask(__name__)

# 0.create connection
mlab.connect()

# new_service = Service(
   
#     name= "Đạt 100 ",
#     yob= 1996,
#     gender=1,
#     height=160,
#     phone="01234874523",
#     address="Trần Duy Hưng",
#     status=True
#  )
# new_service.save()

@app.route('/')
def index():
    
    return render_template('index.html')
@app.route('/search/<gender>')
def search(gender):
    all_service = Service.objects(gender=gender)
    
    return render_template('search.html',all_service=all_service,)
@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('search_customer.html',all_customer=all_customer,gender=1)
@app.route("/admin")
def admin():
    all_service =Service.objects()
    return render_template("admin.html",all_service=all_service)

@app.route("/delete/<service_id>")
def delete(service_id):
    service_to_delete= Service.objects().with_id(service_id)
    if service_to_delete is None:
        return "service not found"
    else:
        service_to_delete.delete()
        return redirect(url_for("admin"))
    
@app.route("/new_service", methods=["GET","POST"])
def new_service():
    if request.method == "GET":
        return render_template("new_service.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        address = form["address"]
        method_service = Service(
            name=name,
            yob=yob,
            address=address
        )
        method_service.save()
        return redirect(url_for("admin"))
# @app.route("/repair_service",methods=["POST"])
# def repair_service():
#     form = request.from
#     name = from["name"]
#     yob





if __name__ == '__main__':
  app.run( debug=True)
 