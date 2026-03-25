import pandas as pd
import random
from faker import Faker

fake = Faker()

products = ["Laptop", "Mobile", "Tablet", "Headphones", "Monitor"]
cities = ["Delhi", "Mumbai", "Hyderabad", "Chennai", "Bangalore"]
categories = ["Electronics", "Accessories"]

data = []

for i in range(1, 501):
    quantity = random.randint(1, 5)
    price = random.randint(1000, 50000)

    record = {
        "OrderID": i,
        "CustomerName": fake.name(),
        "Product": random.choice(products),
        "Category": random.choice(categories),
        "City": random.choice(cities),
        "OrderDate": fake.date_between(start_date='-1y', end_date='today'),
        "Quantity": quantity,
        "Price": price,
        "Total": quantity * price
    }
    data.append(record)

df = pd.DataFrame(data)
df.to_excel("advanced_sales_data.xlsx", index=False)
print("Advanced Excel file created successfully!")