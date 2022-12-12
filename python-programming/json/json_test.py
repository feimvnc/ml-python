'''
python -> json conversion n
dict                object 
list,tuple          array
str                 string
int, long, float    number 
True                true 
False               false 
None                null
'''

import json 
# conver dict to json 
person = {"name": "John", "age": 30, "city": "New York"}
personJSON = json.dumps(person)
print(personJSON)   # {"name": "John", "age": 30, "city": "New York"}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)   # better format 

# save to a file 
with open('person.json', 'w') as file:
    json.dump(person, file, indent = 4)

# deserialization or decoding, convert json string to python object 
person = json.loads(personJSON)
print(person)

# load json file and conver to python object 
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)

# json class 
import json 

class User:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

user = User('Max', 30)

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, "age": o.age, o.__class__.__name__: True}
    else:
        return TypeError('Object of type User is not JSON serializable')  

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, default=encode_user)
print(userJSON)

userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

# also works to encode 
userJSON = UserEncoder().encode(user)
print(userJSON)

# decode object value 
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct 

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)    # Max
