from mongoengine import*

class Order(Document):
    service_id = StringField()
    time = DateTimeField()
    accepted = BooleanField()
    user_id = StringField()
