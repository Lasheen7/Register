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


def receipt(Price):
    print("╔═════════════════════════════════════════╗")
    print("║         𝙁 𝙪 𝙩 𝙪 𝙧 𝙚  𝙈 𝙖 𝙡 𝙡            ║")
    print("║=========================================║")
    print("║                                         ║")
    print(f"║TOTAL PRICE:    {f'{Price:.2f} EGP':<25}║")
    print("║=========================================║")
    print("║                                         ║")
    print("║  𝒯𝒽𝒶𝓃𝓀𝓈 𝒻ℴ𝓇 𝒸𝒽ℴℴ𝓈𝒾𝓃ℊ ℴ𝓊𝓇 ℊ𝓇ℴ𝒸ℯ𝓇𝓎 𝓈𝒽ℴ𝓅!  ║")
    print("╚═════════════════════════════════════════╝")


def discount(T_price):
    if T_price >= 700:
        Sale = T_price 
        Sale -= 0.15 * Sale
        print_delay(f"Here is your total price: {T_price:.2f} EGP")
        print_delay("But you got a 15% discount")
        print_delay(f"So here is the Receipt, Sir:")
        receipt(Sale)
    else:
        print_delay(f"Here is your Receipt, Sir:")
        receipt(T_price)

      
def cashier():
    Total_Price = 0
    print_delay("Welcome to our store !!")
    while True:
        print_delay("What would you like to buy, Sir ?")
        Item = choose_product()
        Item_Index = Products.index(Item)
        Quantity = quant_choice()
        Total_Price += Quantity * Prices[Item_Index]
        print_delay("Anything else, Sir ?")
        Ans = y_n_ans()
        if Ans == "no":
            discount(Total_Price)
            break
    
    
cashier()