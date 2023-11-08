shopping_list = ['milk', 'avokado', 'bananas', 'chocolate', 'nuts']
new_item = input("Ievadi jaunu elementu: ")
shopping_list.append(new_item)

print("Risināsim ar for in")
i = 1
for item in shopping_list:
    print(f"{i}. {item}")
    i += 1

print("Risināsim ar for")
for i in range(len(shopping_list)):
    print(f"{i+1}. {shopping_list[i]}")
