from math import prod
from typing import Optional, List
from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import Product
import json
from dbService import get_all_products
from dbService import get_product_by_id

f = open('../db/MOCK_DATA.json')
db = json.load(f)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/products", response_model=List[Product], status_code=status.HTTP_200_OK)
def get_all_products_from_db():
    return get_all_products()

@app.get("/similar_products/{product_id}", response_model=List[Product], status_code=status.HTTP_200_OK)
def get_similar_products(product_id: str):
    product = get_product_by_id(product_id)
    print(product)
    return [product]