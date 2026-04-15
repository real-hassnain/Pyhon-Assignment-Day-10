products = {
	"Laptop":50000,
	"Mobile":85000,
	"EarBuds":5000
}

print("Products and Prices:")
for name, price in products.items():
    print(name, ":", price)

products["Keyboard"] = 600
products["Laptop"] = 40000


print("Updated Products and Prices:")
for name, price in products.items():
    print(name, ":", price)

total = sum(products.values())
print("Total Price: ", total)