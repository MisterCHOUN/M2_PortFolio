def addition(number1, number2):
    new_number = number1 + number2
    return new_number

# Main

number1 = 2
number2 = 3
number3 = addition(number1, number2)
print("number3 =", number3)

array = [10]

for i in range (0, 10):
    print("i =", i)
    array.append(i)
    if i%2 == 0:
        print("Nombre Pair")
    else:
        print("Nombre Impair")

y = 0
while (y < 10):
    print("array[", y, "] =", array[y])
    y+=1





