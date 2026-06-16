from cryptography.hazmat.primitives.asymmetric import dsa

print("Hello world")
age = 25
print(age, type(age))

name = 'Vignesh'
print(name, type(name))

price = 99.99
print(price, type(price))

is_active = True
print(is_active, type(is_active))

address = None
print(address, type(address))

# Scope of a variable - L->E->G->B
# Local variable - validity of the variable only within that function

#L Local variable
def food_order():
    food = 'Burger'
    print("your food order: " , food)

food_order()
# print(food)
# unresolved reference error , food is a local variable , scope is only within that function

#E enclosed variable
def cart():
    discount = 10 # E -> enclosing variable accessible in nested function

    def checkout():
        print("Checkout discount: ", discount)

    checkout()
cart()

# G global variable
user_id = 'vigrav'

def homepage():
    print('user id: ', user_id)

def profile():
    print('welcome to profile page', user_id)

homepage()
profile()

# B built in - pythons own variable
print(__file__)