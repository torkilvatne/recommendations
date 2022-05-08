import json

f = open('../db/MOCK_DATA.json')
db = json.load(f)

def get_all_products():
    return db[:10]

def get_product_by_id(id: str):
    product = next(filter(lambda x: x.get('id') == id,  db))
    return product