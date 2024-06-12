def display_product(product):
    # tambah barang baru
    # mula2, user dapat key in (opt 1)
    # brapa barang mau key in, so bleh looping 7 kali (opt 2)
    print("Product Name:", product["name"])
    print("Price:", product["price"])
    print("Stock:", product["stock"])

def purchase_product(product, quantity):
    if quantity <= product["stock"]:
        product["stock"] -= quantity
        print("Purchase successful!")
        print("Remaining stock:", product["stock"])
    else:
        print("Insufficient stock!")

def main():
    products = []

    products.append({"name": "Clothes", "price": 50, "stock": 10})
    products.append({"name": "Baju Kurung", "price": 40, "stock": 15})
    products.append({"name": "Skirt", "price": 60, "stock": 8})
    products.append({"name": "Mini Skirt", "price": 55, "stock": 12})
    products.append({"name": "Tudung", "price": 30, "stock": 20})

    print("Item Details:")
    for idx, product in enumerate(products, 1):
        print("Product", idx)
        display_product(product)
        print()

    print("Buyer's Transaction:")
    print("Enter the product index (1-5) you want to purchase:")
    choice = int(input()) - 1
    print("Enter the quantity you want to purchase:")
    quantity = int(input())
    purchase_product(products[choice], quantity)
    
    print("Add items (if not, use "-" ): ")
    

if __name__ == "__main__":
    main()





# class Product:x
# def __init__(self, name, price, stock):
#         self.name = name
#         self.price = price
#         self.stock = stock

# def display(self):
#         print("Product Name:", self.name)
#         print("Price:", self.price)
#         print("Stock:", self.stock)

# def purchase(self, quantity):
#         if quantity <= self.stock:
#             self.stock -= quantity
#             print("Purchase successful!")
#             print("Remaining stock:", self.stock)
#         else:
#             print("Insufficient stock!")

# def main():
#     products = []

#     products.append(Product("Clothes", 50, 10))
#     products.append(Product("Baju Kurung", 40, 15))
#     products.append(Product("Skirt ", 60, 8))
#     products.append(Product("Mini Skirt", 55, 12))
#     products.append(Product("Tudung ", 30, 20))

#     print("Item Details:")
#     for product in products:
#         product.display()
#         print()

#     print("Buyer's Transaction:")
#     print("Enter the product index (1-5) you want to purchase:")
#     choice = int(input()) - 1
#     print("Enter the quantity you want to purchase:")
#     quantity = int(input())
#     products[choice].purchase(quantity)

# if __name__ == "__main__":
#     main()
