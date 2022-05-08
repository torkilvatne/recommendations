import json

f = open('../db/MOCK_DATA.json')
db = json.load(f)

def get_all_products():
    return db[:10]

def get_product_by_id(id: str):
    return next((x for x in db if x.id == id), None)