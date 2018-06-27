from mongoengine import*
# 1.design database

class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

# new_service = Service(
#     name= "Fangqing",
#     yob= 2000,
#     gender=0,
#     height=160,
#     phone="1238473844",
#     address="Hồ Chí Minh",
#     status=True
# )
# new_service.save()
db.Service.remove(Document)