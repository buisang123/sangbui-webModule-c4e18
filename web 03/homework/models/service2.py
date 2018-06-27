from mongoengine import*

class Service(Document):
    name= StringField()
    yob=IntField()
    height=IntField()
    gender=IntField()
    phone=StringField()
    address=StringField()
    description=ListField()
    measurements=ListField()
    status=BooleanField()
