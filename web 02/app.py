from flask import Flask, render_template
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
    all_service = Service.objects(gender=gender,yob__lte=1998,address__icontains="Hà Nội")
    
    return render_template('search.html',all_service=all_service,)
@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('search_customer.html',all_customer=all_customer,gender=1)


if __name__ == '__main__':
  app.run( debug=True)
 