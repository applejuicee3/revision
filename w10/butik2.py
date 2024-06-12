class Products:
    def __init__(self, name, price, stock, ic, age):
        self.name = name
        self.price = float(price)  # Convert price to float
        self.stock = int(stock)    # Convert stock to integer
        self.ic = ic
        self.age = int(age)

    def display(self):
        print("Name  :", self.name)
        print("Price :", str(self.price))  # Convert price to string for concatenation
        print("Stock :", str(self.stock))  # Convert stock to string for concatenation
        print("IC    :", self.ic)
        print("Age   :", str(self.age))    # Convert age to string for concatenation
        print("______________")

    def purchase(self, quantity=1):
        if self.stock >= quantity:
            self.stock -= quantity
            print(f"Transaction completed! Remaining stock: {self.stock}")
        else:
            print("Insufficient stock!")

# Function to add a new product
def add_product(products_list):
    name = input("Name: ")
    price = input("Price: ")
    stock = input("Stock: ")
    ic = input("IC: ")

    while True:  # Keep asking until a valid age is provided
        age = input("Age: ")
        try:
            age = int(age)  # Convert age to integer
            break  # Break the loop if conversion is successful
        except ValueError:
            print("Insert a number for your age")

    product = Products(name, price, stock, ic, age)
    products_list.append(product)
    print("Product added successfully!")

# List to store products
products_list = []

# Adding products loop
while True:
    add_product(products_list)
    choice = input("Add one more product? (yes/no): ")
    if choice.lower() != "yes":
        break

# Print updated products
print("\nUpdated Products:")
for product in products_list:
    product.display()

# Purchase a product
product_index = int(input("Enter the index of the product to purchase: "))
quantity = int(input("Enter the quantity to purchase: "))
if 0 <= product_index < len(products_list):
    products_list[product_index].purchase(quantity)
else:
    print("Invalid product index!")
