from models.service2 import Service
import mlab
mlab.connect()

new_service = Service(
    name="Tuấn Tiền Tỉ",
    yob=1993,
    height=166,
    gender=1,
    phone="0912312783",
    address="Hà Nội",
    description=["tốt bụng","hài hước","diễn sâu"],
    measurements=[80,70,80],
    status=True
)
new_service.save()
