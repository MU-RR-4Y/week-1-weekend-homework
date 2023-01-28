# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop_name):
    return shop_name['name']

def get_total_cash (shop_name):
    return shop_name['admin']['total_cash']

def add_or_remove_cash(shop_name, cash):
    shop_name['admin']['total_cash'] += cash

def get_pets_sold(shop_name):
    return shop_name['admin']['pets_sold']

def increase_pets_sold(shop_name, pets):
    shop_name['admin']['pets_sold'] += pets

def get_stock_count(shop_name):
    return len(shop_name['pets'])

def get_pets_by_breed(shop_name, breed):
    pets_by_breed =[]
    for pet in shop_name['pets']:
        if pet['breed'] == breed:
            pets_by_breed.append(pet)
    return pets_by_breed

def find_pet_by_name(shop_name, name):
    for pet in shop_name['pets']:
        if pet['name'] == name:
            return pet

def remove_pet_by_name(shop_name, name):
    for pet in shop_name['pets']:
        if pet['name'] == name:
            shop_name['pets'].remove(pet)

def add_pet_to_stock(shop_name, new_pet):
    shop_name['pets'].append(new_pet)

def get_customer_cash(customer):
    return customer['cash']

def remove_customer_cash(customer, cash):
    customer['cash'] -= cash

def get_customer_pet_count(customer):
    return len(customer['pets'])

def add_pet_to_customer(customer,new_pet):
    customer['pets'].append(new_pet)

def customer_can_afford_pet(customer,pet):
    can_buy = False
    if customer['cash'] >= pet['price']:
        can_buy = True
    return can_buy

def sell_pet_to_customer(shop_name, pet, customer):
    
    remove_pet_by_name(shop_name,pet['name'])
    remove_customer_cash(customer,pet['price'])
    add_pet_to_customer(customer,pet)
    add_or_remove_cash(shop_name,pet['price'])
    increase_pets_sold(shop_name,len(pet))
    

