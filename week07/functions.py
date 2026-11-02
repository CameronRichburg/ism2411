# Self assessment questions
# 1. the first error that I found was the absent : in "for sales in sales", because that was the first error that popped up when I ran the code. Currently, my debugging instincts have room for improvement.
# 2. the function takes the input of the price and it's discount tier and uses it to return the final price after the applied discount. A colleague could use it if the inputs are presented.
# 3. I used AI to help explain in more detail how to fix the third error. The AI built my understanding since it helped me find the difference when applying = or += to the code.

# --- Exercise 1 ---

# Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax( 100, 0.07)
tax2 = calculate_tax(250, 0.08)

print( f"Tax for $100 at 7%: ${tax1:.2f}")
print( f"Tax for $250 at 8%: ${tax2:.2f}")
print( f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# -- Exercise 2 ---

# Defining a function with multiple parameters

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function with different tiers
original_price = 200

for tier in ["gold","silver","bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# --- Exercise 3 ---

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# Calling the final_price function
print( f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# --- Exercise 4 ---

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# --- Exercise 5 ---
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1
# First error: SyntaxError: expected ':' "for sale in sales" Fix: "for sale in sales:"
# Second error: IndexError: list index out of range print(sales[i]). Fix: The index will start at 0, fix the while loop to have i<len(sales):
# Third error: "total = sale", it produces 90 as the total instead of 715: Fix: change total = sale to total += sale to get the total of the inputs.
# --- Exercise 6 ---

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)