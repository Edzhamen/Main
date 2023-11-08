names = ['Anna', 'Oskars', 'Jennifer']
number = ['123456789', '987654321', '987564321']
new_name = input("Ievadi jaunu vārdu: ")
new_number = input("Ievadi jaunu numuru")
names.append(new_name)
number.append(new_number)

for i in range(len(names)):
    print(f"{names[i]} {number[i]}")
