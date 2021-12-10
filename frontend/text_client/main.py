from urllib.request import urlopen
import json

def print_geocache(geocache):
        print("_id: %s, location: (%f, %f), hint: %s" % (g["_id"]["$oid"], g["lat"], g["lon"], g["hint"]))
        print("image: %s" % g["image"])


print("/geocaches:")
with urlopen("http://localhost:8000/geocaches") as response:
    geocaches = json.loads(response.read())
    for g in geocaches:
        print_geocache(g)
print()


print("/geocaches?hint=inside:")
with urlopen("http://localhost:8000/geocaches?hint=inside") as response:
    geocaches = json.loads(response.read())
    for g in geocaches:
        print_geocache(g)
print()


print("Search logbooks by email (enter email): ", end='')
email = input()
print("/geocaches?email=" + email + ":")
with urlopen("http://localhost:8000/geocaches?email=" + email) as response:
    geocaches = json.loads(response.read())
    for g in geocaches:
        print_geocache(g)
print()
