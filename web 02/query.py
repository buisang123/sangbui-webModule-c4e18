from models.service import Service
import mlab

mlab.connect()

# all_service = Service.objects()
# first_service = all_service[0]
# print(first_service.name)

id_to_find = "5b2ba8946892dc05042f58d8"
# hera = Service.objects().get(id=id_to_find)
service= Service.objects().with_id(id_to_find)
# print(hera.to_mongo())


if service is not None:
    # hera.delete()
    # print("deleted")
    print(service.yob)
    service.update(set__yob=2005)
    service.reload()
    print(service.yob)


else:
    print("service not found")