j = 1
z = 1
for i in range(1,101):
    if (i%(j*3) == 0 and i%(z*5) ==0):
        print("FizzBuzz")
        j += 1
        z += 1
    elif(i == j*3):
        print("Fizz")
        j+= 1
    elif(i == z*5):
        print("Buzz")
        z+= 1

    else:
        print(i)
i+= 1