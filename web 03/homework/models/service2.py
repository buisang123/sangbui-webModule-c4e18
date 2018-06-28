from mongoengine import*

class Service(Document):
    image=StringField()
    name= StringField()
    yob=IntField()
    height=IntField()
    gender=IntField()
    phone=StringField()
    address=StringField()
    description=ListField()
    measurements=ListField()
    status=BooleanField()
