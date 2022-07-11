import random


print("Это игра \"Угадай число\" ")
print("""Правила просты, компьютер загадывает число от
1 до 5\nты пробуешь его угадать""")
print("Поехали !")



while True:
    comp = random.randint(1, 5)
    human = int(input("Введи свое число>   "))

    if comp == human:
        print("Ничего себе, угадал !")
        break

    elif comp != human:
        print("Ты нек угадал, компьютер загадал число " + str(comp))
