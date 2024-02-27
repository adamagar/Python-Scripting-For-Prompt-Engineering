import json

json_data = '{"name":"Adam", "age":32, "city":"LA"}'

data = json.loads(json_data)

age = data["age"]
name = data["name"]
city = data["city"]

print(name)
print(age)