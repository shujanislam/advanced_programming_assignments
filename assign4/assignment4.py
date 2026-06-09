items = [
    {"product": "Pen", "qty": 5},
    {"product": "Notebook", "qty": 20},
    {"product": "Pencil", "qty": 8},
    {"product": "Eraser", "qty": 15},
    {"product": "Marker", "qty": 3}
]

limit = 10

print(f"Products with stock less than {limit}:")

for i in range(len(items)):
    if items[i]["qty"] < limit:
        print(items[i]["product"], "-", items[i]["qty"])
