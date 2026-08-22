import time

Products = ["rice", "chicken", "sugar", "meat", "salt"]
Prices = [35, 150, 40, 500, 10]


def print_delay(message, period=1.5):
    print(message)
    time.sleep(period)


def choose_product():
    product = ''
    print_delay("What would you like to buy, Sir ?")
    while True:
        product = input()
        if product in Products:
            break
        else:
            print_delay("Please choose a valid product, Sir")
    return product
 
            
def cashier():
    print_delay("Welcome to our store !!")
    choose_product()
    
cashier()