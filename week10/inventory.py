# Reflection questions
# 1. The most suprising thing about python lists is how easily they can be changed by things like append and sort. It 
# is also interesting that negative indexing can access the end of a list
# 2. A list would be useful in a situation involving tracking inventory and sales from multiple products. Instead of manually
# Calculating everything, a list cna be used to automatically filter, calculate totals, and update inventory.

# Exercise 1: build a list
print("--- Exercise 1: Build a list ---")

inventory = ("pen","notebook","stapler","tape","marker")
print(inventory)
print(len(inventory))

#Exercise 2: Index Practice

print("--- Exrcise 2: Index Practice ---")
print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle])

print("--- Exercise 3: List slicing ---")

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

print("--- Exercise 4: List Methods ---")

inventory.append("envelope")
inventory.append("tape")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

print(" --- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060)

coords[0] = 99
try:
    coords [0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident")

    print(" --- Exercise 6: List Average Sales ---")
    sales = [100, 250, 75, 480, 200]
    total = sum(sales)
    count = len(sales)
    average = total / count
    print(f"Total sales: {total}")
    print(f"Number of sales: {count}")
    print(f"Average sales: {average}")
    print(f"Best sale: {max(sales)}")
    print(f"Worst sale: {min(sales)}")

    best = sales[0]
    worst = sales[0]

    for amount in sales:
        if amount > best:
            best = amount
            if amount < worst:
                worst = amount

print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")

print("--- Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))

print(prices)
print(discounted)

print("--- Exercise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))
