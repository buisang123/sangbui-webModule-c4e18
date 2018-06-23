from models.customer import Customer
import mlab
from faker import Faker
from random import randint,choice
mlab.connect()

fake = Faker()
# print(fake.name())

for j in range(30):
    print("Saving customer",i+1,"...")
    new_customer = Customer(
        name= fake.name(),
        yob=randint(1980,2000),
        gender=randint(0,1),
        height=randint(155,190),
        phone= fake.phone_number(),
        address=fake.address(),
        status=choice([True,False])
        job=fake.job()

    
)
    new_customer.save()