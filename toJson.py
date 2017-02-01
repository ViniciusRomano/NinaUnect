import json
from CrudNina import CrudNina


crud = CrudNina()
somedict = crud.getAll()

with open('result.json', 'w') as fp:
    json.dump(somedict, fp)
