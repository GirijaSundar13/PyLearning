import json

def validate_json(json_object):
    try:
        result = json.loads(json_object)
    except Exception as e:
        print("Invalid Json.", e)
    else:
        print("Valid Template")

json_obj = r'''
{
    "customer": "customerInfo",
    "service-z-end": {
        "rx-direction": {
            "port": {
                "port-device-name": "router-22",
                "port-name": "R1",
                "a" : null,
                "b" : null
            },
            "Restorable" : true,
            "Revertible" : false
        }
}
}
'''

validate_json(json_obj)
filename = r'temp.txt'

with open(filename) as f:
    contents = f.read()
validate_json(contents)



