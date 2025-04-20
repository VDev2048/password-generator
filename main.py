import random

length = int(input())

def Generate(length : int) -> str:
    new = []
    letters = "abcdefghijklmnopqrstuvwxyz"
    m_numbers = "0123456789"
    symbols = "!@#$%^&*()/-:<>.,?"
    for i in range(length):
        new.append(letters[random.randint(0,len(letters)-1)])

    for j in range(len(new)):
        if j % 2 == 0:
            new[j] = new[j].upper()
    for a in range(len(new)):
        if a % 3 == 0:
            new[a] = m_numbers[random.randint(0,len(m_numbers)-1)]
        if a % 5 == 0:
            new[a] = symbols[random.randint(0, len(symbols) - 1)]

    return "".join(new)
print(Generate(length))
