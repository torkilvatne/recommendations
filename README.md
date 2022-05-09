# Basic Recommendations
Basic recommendation algorithms for products.

## Setup API

Locate repo in terminal window and run following commands to set up FastAPI.

```sh
$ cd api
$ pip install -r requirements.txt
$ uvicorn api:app --reload
```

## URLs

- http://127.0.0.1:8000/products
- http://127.0.0.1:8000/similar_products/{product_id}