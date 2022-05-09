from dbService import get_all_products
from schemas import Product
import math

COMPARISON_VALUES_NUMERICAL = ['price']

def find_product_to_recommend(base_product: Product):
    # Get all products
    db = get_all_products()

    # Loop through products and if similarity-score is higher than set product -> replace
    current_score = 0
    current_product = None
    for product in db:
        print(product)
        if (product['id'] == base_product.id):
            continue
        similarity_score = cosine_similarity(base_product, product)
        print(similarity_score + " for " + product.id)
        if (similarity_score > current_score):
            current_score = similarity_score
            current_product = product

    # Logging
    print("Highest score:")
    print(current_score)
    print("Most similar product: ")
    print(current_product)

    # Return most similar product
    return current_product

# https://towardsdatascience.com/cosine-similarity-explained-using-python-machine-learning-pyshark-5c5d6b9c18fa
# https://towardsdatascience.com/find-similar-products-to-recommend-to-users-8c2f4308c2e4
# https://towardsdatascience.com/comprehensive-guide-on-item-based-recommendation-systems-d67e40e2b75d
# https://medium.com/analytics-vidhya/cosine-similarity-between-products-to-recommend-similar-products-3b94bf6e30ba
def cosine_similarity(i: Product, j: Product):
    # Nominator
        # (i · j) = (i1 × j1) + (i2 × j2) + ... + (in × jn)
    nominator = 0
    for comparison_value in COMPARISON_VALUES_NUMERICAL:
        nominator += get_product_value_of(i, j, comparison_value)
    
    # Denominator
        # ||i|| × ||j|| = sqrt(i1^2 + i2^2 + ... + in^2) × sqrt(j1^2 + j2^2 + ... + jn^2)
    denominator = get_length_of_vector(i) * get_length_of_vector(j)

    # Complete formula
        # Nominator / Denominator
    similarity = nominator / denominator

    return similarity

def get_product_value_of(i, j, key):
    return i[key] * j[key]

def get_length_of_vector(product):
    sum_of_values = 0
    for key in COMPARISON_VALUES_NUMERICAL:
        sum_of_values += product[key]**2
    return math.sqrt(sum_of_values)