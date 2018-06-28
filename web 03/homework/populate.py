from models.service2 import Service
import mlab
mlab.connect()

new_service = Service(
    image="https://genknews.genkcdn.vn/2017/photo-4-1490609870810.jpg",
    name="Linh Ngọc Đàm",
    yob=1995,
    height=166,
    gender=0,
    phone="0928347563",
    address="Hà Nội",
    description=["xinh gái","cute","ngoan hiền"],
    measurements=[80,70,80],
    status=True
)
new_service.save()
