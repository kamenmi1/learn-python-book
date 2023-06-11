# working with arbitrary number of arguments

#pizza.py
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'salami', 'pineapple')

#using arbitrary keyword arguments
#user_profile.py

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about the user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', field='physics')

# print(user_profile)

#Try it yourself
#8-12. Sandwiches

def make_sandwich(*items):
    """Print out what items will be on the sandwich."""

    for item in items:
        print(f"- adding on top of the sandwich: {item}")


# make_sandwich('salami')
# make_sandwich('peper', 'tomato', 'ketchup', 'cheese')

#8-13. User profile
def building_my_profile(first, last, **kwargs):
    kwargs['first_name'] = first
    kwargs['last_name'] = last

    return kwargs

my_profile = building_my_profile('Milo', 'Ka', hobby = 'bee_keeping', favorite_pizza = 'hawai')

# print(my_profile)

#8-14. Cars

def make_car(brand, model, **additional):
    additional['brand'] = brand
    additional['model'] = model

    return additional

car = make_car('Subaru', 'Outback', color='blue', tow_package = True)

# print(car)

#8.15 Printing models

# import printing_functions

# printing_functions.print_me('milo')

# import printing_functions as pf

from printing_functions import print_me as pm

pm('Milo')