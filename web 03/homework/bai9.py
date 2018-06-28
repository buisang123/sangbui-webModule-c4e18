from models.river import River
import mlab7

mlab7.connect()

all_river_s = River.objects(continent="S. America",length=1000)

for river2 in all_river_s:
    print(river2.name)
    print()