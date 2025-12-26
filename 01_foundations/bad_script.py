import json

data = '{"name": "Sandeep", "age": 38, "active": true}'

user = json.loads(data)

if user["age"] > 18:
    print("User is adult")
else:
    print("User is minor")

print("Process completed")
