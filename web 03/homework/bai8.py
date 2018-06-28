from models.river import River
import mlab7

mlab7.connect()
all_river = River.objects(continent="Africa")

for river in all_river:
    print(river.name)
    print()