my_name = "Yusuf Eren Nalbant"
my_id = "220104004049"
my_email = "y.nalbant2022@gtu.edu.tr"

def problem1 ():
    return my_name[0]

def problem2 ():
    index = int(input("Enter a number:"))
    if(index < 0 or index > len(my_name)-1):
        index = index % len(my_name)
        return my_name[index]
    else:
        return my_name[index]

def problem3 ():
    minIndex = int(input("Enter first number:"))
    maxIndex = int(input("Enter second number:"))
    if(minIndex <= maxIndex) :
            if(maxIndex > len(my_name) - 1):
                maxIndex = maxIndex % (len(my_name))
            if(minIndex > len(my_name) - 1):
                minIndex = minIndex % (len(my_name))
            if(minIndex < 0):
                minIndex = minIndex % len(my_name)
            if(minIndex > maxIndex):
                return my_name[maxIndex : minIndex +1]
            return (my_name[minIndex : maxIndex + 1])
    else:
        print("it mustn't be minIndex > maxIndex")

def problem4 ():
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    letter = input("Enter input:")
    if (len(letter) <= 100 and len(letter) >= 1) :
        for i in letter:
            if i in vowels:
                count += 1
        return count
    else:
        return 0

def problem5 ():
    i = 0
    for j in my_id:
        i += int(j)
    return i

def problem6 ():
    k = 1
    j = 1
    number = int(input("Enter input:"))
    if(number >= 0 and number <= 30):
        if (number == 0):
            return 1
        elif (number == 1):
            return 1
        elif (number < 0):
            return 0
        else :
         while (j <= number):
             k *= j
             j += 1
        return (k)

def problem7 ():
    number = int(input("Enter a number:"))
    if(number % 3 == 0 and number % 7 == 0):
        return True
    else:
        return False

def problem8 ():
    number = int(input("Enter a number:"))
    if (number % 3 == 0 and number % 7 != 0):
        return 1
    elif (number % 3 != 0 and number % 7 == 0):
        return 2
    elif (number % 3 == 0 and number % 7 == 0):
        return 3

def problem9 ():
    number = float(input("Enter a number:"))
    k = 2
    if(number == 2):
        return True
    while (k < number):
        if(number % k == 0):
            return False
        else:
            k += 1
    return True

