from acme import Product
from random import randint, uniform, choice

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']

def random_name():
    return choice(ADJECTIVES) + " " + choice(NOUNS)

def random_price_weight():
    return randint(5, 100)

def random_flammability():
    return uniform(0.0, 2.5)

def generate_products(num_prods=30):
    products = []
    for _ in range(num_prods):
        products.append(Product(random_name(), random_price_weight(), random_price_weight(), random_flammability()))
    return products

def inventory_report(products):
    unique_names = []
    average_price = 0
    average_weight = 0
    average_flammability = 0

    for product in products:
        if product.name not in unique_names:
            unique_names.append(product.name)
        average_price += product.price
        average_weight += product.weight
        average_flammability += product.flammability
    
    average_price = average_price / len(products)
    average_weight = average_weight / len(products)
    average_flammability = average_flammability / len(products)

    print('OFFICIAL ACME INVENTORY REPORT')
    print('INTERNAL USE ONLY')
    print(f'The inventory has {len(unique_names)} unique product names.')
    print(f'The average price of products is: {average_price}')
    print(f'The average weight of products is: {average_weight}')
    print(f'the average flammability of products is: {average_flammability}')


if __name__ == '__main__':
    inventory_report(generate_products())