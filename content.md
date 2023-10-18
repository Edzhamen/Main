## Izveidot number guessing spēli ar Python programēšaas valodu

### Saturs

### 1. Aprakstīt spēli
### 2. Spēles loģika

Dators nejauši ģenerē vienu skaitli no 1 līdz 100. Tālāk, piedāvā spēlētājam uzminēt to skaitli. Un t. t.
Spēles loģika ir aprakstita šeit:

import random

repeat = True

while repeat:
    number = random.randint(1, 100)
    guess = 0
    tries = 0

    while guess != number:
        if guess < number:
            print("Pamēģini lielāku skaitli.")
        else:
            print("Pamēģini mazāku skaitli.")

        guess = int(input("Uzmini skaitli: "))
        tries += 1
    else:
        if tries < 4:
            print(f"WOW! uzminēji tikai pēc {tries} reizēm!")
        elif tries < 7:
            print(f"Nav slikti, uzminēji pēc {tries} reizēm!")
        else:
            print(f"Hm... vajadzētu patrenēties, uzminēji pēc {tries} reizēm!")

    response = input("Vai gribi turpināt? y/n: ")    
    if response == "y":
        repeat = True
    elif response == "n":
        repeat = False
        print("Paldies par spēli! Bye, bye!")
    else:
        repeat = False
        print("Paldies par spēli!  Bye, bye!")
### 3. Un t. t.
