import enum
from dbService import get_all_products
from schemas import Product
import math

COMPARISON_VALUES_NUMERICAL = ['price']
COMPARISON_VALUES_CATEGORICAL = ['category', 'production_location']
N = 5

def find_product_to_recommend(base_product: Product):
    # Get all products
    db = get_all_products()

    # List of products with similarity score
    similarity_scores = []
    for product in db:
        if (product['id'] == base_product['id']):
            continue
        similarity_scores = insort(similarity_scores, product, cosine_similarity(base_product, product))

    # Return most similar product
    similarity_scores.sort(key=lambda x: x['similarity_score'], reverse=True)
    return similarity_scores

# https://towardsdatascience.com/cosine-similarity-explained-using-python-machine-learning-pyshark-5c5d6b9c18fa
# https://towardsdatascience.com/find-similar-products-to-recommend-to-users-8c2f4308c2e4
# https://towardsdatascience.com/comprehensive-guide-on-item-based-recommendation-systems-d67e40e2b75d
# https://medium.com/analytics-vidhya/cosine-similarity-between-products-to-recommend-similar-products-3b94bf6e30ba
def cosine_similarity(i: Product, j: Product):
    # Nominator
        # (i · j) = (i1 × j1) + (i2 × j2) + ... + (in × jn)
    nominator = 0
    for comparison_value in COMPARISON_VALUES_NUMERICAL:
        nominator += get_product_value_of_numerical(i, j, comparison_value)
    for comparison_value in COMPARISON_VALUES_CATEGORICAL:
        nominator += get_product_value_of_categorical(i, j, comparison_value)
    
    # Denominator
        # ||i|| × ||j|| = sqrt(i1^2 + i2^2 + ... + in^2) × sqrt(j1^2 + j2^2 + ... + jn^2)
    denominator = get_length_of_vector(i) * get_length_of_vector(j)

    # Complete formula
        # Nominator / Denominator
    similarity = nominator / denominator

    return similarity

def get_product_value_of_numerical(i, j, key):
    return i[key] * j[key]

def get_product_value_of_categorical(i, j, key):
    return 1 if i[key] == j[key] else 0

def get_length_of_vector(product):  
    sum_of_values = 0
    for key in COMPARISON_VALUES_NUMERICAL:
        sum_of_values += product[key]**2
    for key in COMPARISON_VALUES_CATEGORICAL:
        sum_of_values += 1**2
    return math.sqrt(sum_of_values)

def insort(li, p, sc):
    p['similarity_score'] = sc
    if len(li):
        li.append(p)
    else:
        i = 0
        for index, value in enumerate(li):
            if value['similarity_score'] < sc:
                i = index
                break
        li.insert(i, p)
    return li[:N]