def project1 ():
    inputChoice = {'w','e','n','s'}
    order = input("Enter the exit route: ")
    x = 0
    y = 0
    if len(order) >= 1 and len(order) <= 200:
        for location in order:
            if location in inputChoice:
                if location == 's':
                    y -= 1
                elif location == 'w':
                    x -= 1
                elif location == 'e':
                    x += 1
                elif location == 'n':
                    y += 1
            else:
                print("invalid input")
                break
        result = abs((x ** 2) + (y ** 2))
        result = babil_guess(result)
        return result

def babil_guess(number):
    guess = 1
    iteration = 1000000
    x = number
    i = 0
    while i <= iteration:
        guess = (guess + (x / guess)) * 0.5
        i += 1
    return guess

