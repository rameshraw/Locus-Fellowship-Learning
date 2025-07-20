import json
newdata={
    "id": 100,
    "name": "Software Fellow 100",
    "age": 35
       
}

with open('users.json', 'r') as file:
       data = json.load(file)
       print(data)

with open('users.json', 'w') as file:
       data.append(newdata)
       json.dump(data,file,indent=2)