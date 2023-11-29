phonebook = []

while True:
    choice = input("1-pievienot, 2-izvadīt visus ierakstus, 3-izdzēst, 4-iziet: ")

    if choice == "1":
        # UZDEVUMS 1
        # Saglabā vārdu un numuru
        # - kā piepras;it vārdu un numuru?
        # - kur saglabāt tos datus?
        name = input("Uzraksti vārdu: ")
        number = input("Uzraksti numuru: ")
        person = {
            "name": name,
            "number": number
        }
        phonebook.append(person)
        
    elif choice == "2":
        # UZDEVUMS 2
        # Izvadīt visus datus
        for person in phonebook:
            print(f"{person['name']}: {person['number']}")
        
    elif choice == "3":
        #izdzēst
        pass
    elif choice == "4":
        print("Bye, thanks for using our phonebook!")
        exit()
    else:
        print("Nebija pareiza izvēle")
