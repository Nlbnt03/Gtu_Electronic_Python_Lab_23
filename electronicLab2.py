def problem1 ():
    fahrenheit = float(input("Enter Fahrenheit degree: "))
    if (fahrenheit <= 200.0 and fahrenheit >= -100.0):
        celcius = (fahrenheit - 32) / 1.8000
        return celcius
    else:
        print("input must be input >= -100.0 and input <= 200.0")

def problem2 ():
    celcius = float(input("Enter Celcius degree: "))
    if (celcius >= -100.0 and celcius <= 100.0):
        fahrenheit = (celcius * 1.8000) + 32
        return fahrenheit
    else:
        print("input must be input >= -100.0 and input <= 100.0")

def problem3 ():
    number = int(input("Enter a number: "))
    if (number <= 1E6 and number >= 1):
        result = 2 * (number ** 2) - number
        return result
    else :
        print("input must be input >= 1 and input <= 1E6")

def problem4 ():
    a = 0
    b = 0
    result = []
    number = int(input("Enter a number: "))
    if (number == 0):
        return 2
    elif (number == 1):
        return 1
    else:
        while(b <= number):
            if (b == 0):
                result.append(2)
                b += 1
            elif (b == 1):
                result.append(1)
                b += 1
            else:
                result.append(result[b - 1] + result[b - 2])
                b += 1
        return result[number]

def problem5 ():
    sentence = input("Enter a string: ")
    if (len(sentence) >= 1 and len(sentence) <= 100):
        return sentence[:: -1]
    else:
        print("input's lenght must be input >= 1 and input <= 100")

def problem6 ():
    sentence = input("Enter a string: ")
    a = 0
    empty = []
    if (len(sentence) >= 1 and len(sentence) <= 100):
        for char in sentence:
            if (char >= '0' and char <= '9'):
                empty.append(sentence[a])
                a += 1
            elif (char <= 'z' and char >= 'a'):
                empty.append(sentence[a])
                a += 1
            elif (char <= 'Z' and char >= 'A'):
                empty.append(sentence[a])
                a += 1
            else:
                a += 1
        result = "".join(empty)
        return result
    else:
        print("input's lenght must be input >= 1 and input <= 100")

def problem7 ():
    number = int(input("Enter input: "))
    if(number >= -1E6 and number <= 1E6):
        Newnumber = abs(number)
        strnbr = str(Newnumber)
        empty = []
        result = ""
        a = 0
        for letter in strnbr:
            empty.append(letter)
        while (empty[a] == "0"):
            empty.pop(a)
            a += 1
        strnbr = "".join(empty)
        newNbr = int(strnbr)
        newEmpty = []
        while (newNbr // 4 >= 0):
            newEmpty.append(str(newNbr % 4))
            newNbr = newNbr // 4
            if (newNbr == 0):
                break
        if (number < 0):
            return ("-" + ("".join(newEmpty)[::-1]))
        else:
            return ("".join(newEmpty)[::-1])
    else:
        print("input must be input >= -1E6 and input <= 1E6")
def problem8 ():
    inputs = input("Enter input:")
    sets = {"}":"{", ")":"(", "]":"["}
    empty = []
    for char in inputs:
        if char in sets.values():
            empty.append(char)
        elif char in sets.keys():
            if not empty or empty.pop() != sets[char]:
                return False

    return not empty

def problem9 ():
    sentence = input("Enter a string: ")
    empty = []
    if (len(sentence) >= 1 and len(sentence) <= 200):
        a = len(sentence) - 1
        while(sentence[a] != " " and a >= 0):
            empty.append(a)
            a -= 1
        return len(empty)
    else:
        print("input's lenght must be input >= 1 and input <= 200")
