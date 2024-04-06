import json


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_json(self):
        return json.dumps(self.__dict__, sort_keys=True, indent=4)


def from_json(json_data):
    data = json.loads(json_data)
    return Product(data['name'], data['price'], data['quantity'])


# Creating some Product objects
products = [
    Product("Laptop", 999.99, 5),
    Product("Phone", 699.99, 10),
    Product("Tablet", 299.99, 20)
]

# Serialize the products and write to a file
with open("products.json", "w") as file:
    file.write("[\n")
    for i, product in enumerate(products):
        if i > 0:
            file.write(",\n")
        file.write(product.to_json())
    file.write("\n]")

# Read the serialized products from the file and deserialize
deserialized_products = []
with open("products.json", "r") as file:
    data = json.load(file)
    for item in data:
        deserialized_product = from_json(json.dumps(item))
        deserialized_products.append(deserialized_product)

# Print all product information
for product in deserialized_products:
    print(product.to_json())
