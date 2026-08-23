import time

Products = ["rice", "chicken", "sugar", "meat", "salt"]
Prices = [35, 150, 40, 500, 10]


def print_delay(message, period=1.5):
    print(message)
    time.sleep(period)


def choose_product():
    product = ''
    while True:
        product = input()
        if product in Products:
            break
        else:
            print_delay("Please choose a valid product, Sir")
    return product


def quant_choice():
    quant = ''
    Q = [str(z) for z in range(1, 101)]
    print_delay("How much Kgs do you need, Sir ?")
    while True:
        quant = input()
        if quant in Q:
            return int(quant)
            break
        else:
            print_delay("Please choose a valid quantity")
    return quant


def y_n_ans():
    ans = ''
    Answer = ["yes", "no"]
    while True:
        ans = input()
        if ans in Answer:
            break
        else:
            print_delay("Please answer with yes or no")
    return ans

      
def cashier():
    print_delay("Welcome to our store !!")
    while True:
        print_delay("What would you like to buy, Sir ?")
        Product = choose_product()
        Product_Index = Products.index(Product)
        Quantity = quant_choice()
        Total_Price = Quantity * Prices[Product_Index]
        print_delay("Anything else, Sir ?")
        Ans = y_n_ans()
        if Ans == "no":
            print_delay(f"Here is your total price: {Total_Price} EGP")
            break
        else:
            print_delay(f"Here is your total price: {Total_Price} EGP")
    
    
cashier()