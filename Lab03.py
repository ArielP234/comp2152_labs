# ---------- Question 1 ----------
print("\n--- Question 1: Student Grades List ---")

grades = [85, 92, 78, 95, 88]
grades.append(90)
grades.sort()

print(f"Sorted grades: {grades}")
print(f"Highest grade: {grades[-1]}")
print(f"Lowest grade: {grades[0]}")
print(f"Total number of grades: {len(grades)}")


# ---------- Question 2 ----------
print("\n--- Question 2: Shopping Cart ---")

cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

print(f"Number of apples: {cart.count('apple')}")
print(f"Position of milk: {cart.index('milk')}")

cart.remove("apple")
removed_item = cart.pop()

print(f"Removed item using pop: {removed_item}")
print(f"Is banana in cart? {'banana' in cart}")
print(f"Final cart: {cart}")


# ---------- Question 3 ----------
print("\n--- Question 3: Coordinate System ---")

point1 = (3, 5)
point2 = (7, 2)

x1, y1 = point1
x2, y2 = point2

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

chars = tuple("PYTHON")

print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
print(f"x1: {x1}, y1: {y1}")
print(f"x2: {x2}, y2: {y2}")
print(f"Distance between points: {distance}")
print(f"Characters tuple: {chars}")

for ch in chars:
    print(ch)


# ---------- Question 4 ----------
print("\n--- Question 4: Class Attendance ---")

monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")

both = monday_class.intersection(wednesday_class)
either = monday_class.union(wednesday_class)
only_monday = monday_class.difference(wednesday_class)
only_one_class = monday_class.symmetric_difference(wednesday_class)
is_subset = monday_class.issubset(either)

print(f"Monday class: {monday_class}")
print(f"Wednesday class: {wednesday_class}")
print(f"Attended both classes: {both}")
print(f"Attended either class: {either}")
print(f"Only Monday: {only_monday}")
print(f"Only one class (not both): {only_one_class}")
print(f"Is Monday subset of all students? {is_subset}")


# ---------- Question 5 ----------
print("\n--- Question 5: Contact Book ---")

contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

print(f"Alice's number: {contacts['Alice']}")

contacts["Diana"] = "555-4321"
print(f"Contacts after adding Diana: {contacts}")

contacts["Bob"] = "555-0000"
print(f"Contacts after updating Bob: {contacts}")

del contacts["Charlie"]
print(f"Contacts after deleting Charlie: {contacts}")

print(f"All names: {contacts.keys()}")
print(f"All numbers: {contacts.values()}")
print(f"Total contacts: {len(contacts)}")


# ---------- Question 6 ----------
print("\n--- Question 6: Inventory Management System ---")

inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}

print("\n--- Current Inventory ---")
for product, (price, qty) in inventory.items():
    print(f"{product} - Price: ${price:.2f}, Quantity: {qty}")

electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}

all_products = electronics.union(accessories)
print(f"\nAll product categories: {all_products}")

price_list = [price for price, qty in inventory.values()]
print(f"Price list: {price_list}")

price_list.sort()
print(f"Sorted prices: {price_list}")
print(f"Lowest price: ${price_list[0]:.2f}")
print(f"Highest price: ${price_list[-1]:.2f}")

inventory["Headphones"] = (49.99, 20)

mouse_price, _ = inventory["Mouse"]
inventory["Mouse"] = (mouse_price, 12)

del inventory["Monitor"]

print("\n--- Final Inventory ---")
for product, (price, qty) in inventory.items():
    print(f"{product} - Price: ${price:.2f}, Quantity: {qty}")