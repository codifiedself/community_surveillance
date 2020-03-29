import csv
from webapp.models import State, District
with open('districts.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['district'], flush=True)
        st = State.objects.filter(name=row['state']).first()
        dis = District(name=row['district'], state=st)
        dis.save()