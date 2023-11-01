import random

pcNum = random.randint(1, 100)
count = 2
print(f"Computer Number : {pcNum}")

while True:
    myNum = int(input("My Number : "))
    if(count > 0):
        if myNum == pcNum:
            print("Congrats!")
            break
        elif myNum > pcNum:
            print(f"Turn : {count}")
            print("decrease")
            count -= 1
        else:
            print(f"Turn : {count}")
            print("increase")
            count -= 1
    else:
        print("Lost!")
        break

