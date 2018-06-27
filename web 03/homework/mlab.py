import mongoengine

# mongodb://sangbui:sang1998@ds163530.mlab.com:63530/muadongkhonglanh

host = "ds163530.mlab.com"
port = 63530
db_name = "muadongkhonglanh"
user_name = "sangbui"
password = "sang1998"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())