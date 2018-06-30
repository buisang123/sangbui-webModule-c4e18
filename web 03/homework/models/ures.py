from mongoengine import*

class User(Document):
    fullname=StringField()
    email = EmailField()
    name_login_in= StringField()
    password = StringField()
