count_items = int(input("Number of parcels: "))
weight_items = []

while count_items != 0:
    product_weight = float(input(f"Parcel weight: "))
    if product_weight > 10 or product_weight < 1:
        break
    else:
        weight_items.append(product_weight)
        count_items -= 1

weight_box = 0
boxes = []

for weight in weight_items:
    if weight_box + weight <= 20:
        weight_box += weight
    else:
        boxes.append(weight_box)
        weight_box = weight
boxes.append(weight_box)

result = (f'Result:\n'
          f'Number of packages sent: {len(boxes)}\n'
          f'Number of kilos shipped: {sum(boxes)} kg.\n'
          f'Sum of "empty" kilograms: {(len(boxes)) * 20 - (sum(boxes))} kg.\n'
          f'Package most “empty” kilograms: {(boxes.index(min(boxes)) + 1)}\n'
          f'Weight of this pack: {(min(boxes))} kg.')
print(result)
