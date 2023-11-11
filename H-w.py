import random

random = random.randint(1, 100)
print("Я загадав число ти маєш 5 спроб")
tries = 5

while tries > 0:
    number1 = int(input("Ведіть число "))
    if random == number1:
        print("Ви вгадали")
        break
    if random > number1:
        print("Ваше число замале")
    if random < number1:
        print("Ваше число завелике")
    tries -= 1
    if tries == 0:
        print("Ви програли")