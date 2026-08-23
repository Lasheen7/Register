# Future Mall Cashier System

A command-line grocery store system built in Python for Hack Club's Stardance. 

Most terminal calculators just instantly dump text on the screen, so I built this to feel more like an actual interaction. It uses delayed printing to pace the text, handles input errors gracefully, and generates a formatted receipt at the end.

## How it works

- **Forgiving inputs:** The script cleans up user inputs with `.lower().strip()`, so if you accidentally type " RICE " or "Chicken", the program won't break.
- **Dynamic cart:** Keeps a running total of your items and calculates prices based on quantity.
- **Automatic discounts:** If the final total hits 700 EGP or more, a 15% discount is automatically applied before checkout.
- **ASCII checkout:** Uses nested f-strings to generate a perfectly aligned receipt box with exactly 2-decimal precision for the price.

## Running it locally

You just need Python installed. Clone the repo and run the file:

```bash
git clone [https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git)
cd YOUR-REPO-NAME
python cashier.py