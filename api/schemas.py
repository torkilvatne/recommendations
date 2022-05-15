from pydantic import BaseModel

class ProductBase(BaseModel):
    id:str
    product_name:str
    category:str
    price:int
    production_location:str

class Product(ProductBase):

    class Config:
        orm_mode = True

class SimilarityProduct(ProductBase):
    similarity_score:str

    class Config:
        orm_mode = True