import mongoengine

# mongodb://sangbui:sangbui98@ds121341.mlab.com:21341/video


host = "ds121341.mlab.com"
port = 21341
db_name = "video"
user_name = "sangbui"
password = "sangbui98"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())