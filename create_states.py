import csv
from webapp.models import State
with open('states.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = State(name=row['state'])
        p.save()