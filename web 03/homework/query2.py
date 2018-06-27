from models.service2 import Service
import mlab
mlab.connect()
all_service2 = Service.objects()