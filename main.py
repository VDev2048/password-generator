import random
import sys

print("Введите длину пароля:")
length = int(input())
if(length < 0):
    print("Как ты это себе представляешь...")
    sys.exit()
if(length == 0):
    print("Вот твой пароль:  ")
    sys.exit()
print("Введите сложность пароля (от 1 до 4):")
hardness = int(input())
if(hardness < 1):
    print("ОТ 1 ДО 4 (намек на то, что ты...)")
    sys.exit()
print("Сохранить в файл? (Да - 1, Нет - 0)")
isfile = int(input())
def Generate(length : int) -> str:
    new = []
    letters = "abcdefghijklmnopqrstuvwxyz"
    m_numbers = "0123456789"
    symbols = "!@#$%^&*()/-:<>.,?"
    for i in range(length):
        new.append(letters[random.randint(0,len(letters)-1)])

    if(hardness > 1):
        for j in range(len(new)):
            if j % 2 == 0:
                new[j] = new[j].upper()
    for a in range(len(new)):
        if(hardness > 2):
            if a % 3 == 0:
                new[a] = m_numbers[random.randint(0,len(m_numbers)-1)]
        if (hardness > 3):
            if a % 5 == 0:
                new[a] = symbols[random.randint(0, len(symbols) - 1)]

    return "".join(new)
if(isfile == 0):
    print(Generate(length))
elif(isfile == 1):
    with open("password.txt",'x') as new:
        new.write(Generate(length))
