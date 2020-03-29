import csv
from webapp.models import District, Taluk
with open('taluks.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['taluk'], flush=True)
        dis = District.objects.filter(name=row['district']).first()
        taluk = Taluk(name=row['taluk'], district=dis)
        taluk.save()