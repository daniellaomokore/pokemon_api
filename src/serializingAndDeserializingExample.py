"""
This is an example of derserialization and serialization.

LOADS - deserializing
DUMPS - serializing example

"""

import json

### Json string:
# has single quotation marks around whole thing

### Python dicts
# are ordered, changeable and don't allow duplicates

# LOADS - deserializing
json1 = '{"platform":"nokia", "ip":1111}'     # json string
dict1 = json.loads(json1)   # turns json string into python dictionary that can be now accessed


print(type(json1))  # json string type
print(type(dict1))  # python dict type
print(dict1)        # printing the python dict
#print(dict1['ip'])  # accessing and printing the key's value from the dict


# DUMPS - serializing
dict2 = {"tree": "daffodil",
         "food": "water"
         }    # python dict
json2 = json.dumps(dict2, indent=6)   # turns python dictionary into json string

print(type(dict2))  # python dict type
print(type(json2))  # json string type
print(json2)        # printing the json string




