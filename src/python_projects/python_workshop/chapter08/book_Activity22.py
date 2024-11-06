# Activity 22: Debugging Sample Python Code for an Application
# Consider the following scenario: you have a program that creates a picnic basket for
# you. The baskets are created in a function that depends on whether the user wants
# a healthy meal and whether they are hungry. You provide a set of initial items in the
# basket, but users can also customize this via a parameter.
# A user reported that they got more strawberries than expected when creating multiple
# baskets. When asked for more information, they said that they tried to create a healthy
# basket for a non-hungry person first, and a non-healthy basket for a hungry person
# with just "tea" in the initial basket. Those two baskets were created correctly, but when
# the third basket was created for a healthy person who was also hungry, the basket
# appeared with one more strawberry than expected.



def create_picnic_basket(healthy, hungry, initial_basket=None):
    basket = initial_basket
    if basket == None:
        basket = ["orange", "apple"]

    if healthy:
        basket.append("strawberry")
    else:
        basket.append("jam")

    if hungry:
        basket.append("sandwich")
    return basket

# Reproducer
print("First basket:", create_picnic_basket(True, False))
print("Second basket:", create_picnic_basket(False, True, ["tea"]))
print("Third basket:", create_picnic_basket(True, True))
