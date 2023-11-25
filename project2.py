def problem1(i,j):
    if (j <= i):
        if (i == 1 and j == 1):
            return (1)
        elif (i > 1 and j == 1):
            return (3)
        elif (i > 1 and j == i):
            return (2)
        else:
            return problem1(i - 1, j) + problem1(i - 1, j - 1)
    else:
        return (0)
    
def problem2 (input1, input2):
    similarity = 0
    a = len(input1)
    b = len(input2)
    index = 0
    if (a < b):
        while (index < a):
            if(input1[index] == input2[index]):
                similarity += 1
            index += 1
    elif (b < a):
        while (index < b):
            if(input1[index] == input2[index]):
                similarity += 1
            index += 1
    else:
        while (index < a):
            if (input1[index] == input2[index]):
                similarity += 1
            index += 1
    return (similarity)

def problem3(accounts, source, destination, lira, kurus, fee=True):
    new_accounts = []
    j = 0
    k = 0
    while(j < len(accounts)):
        a = float(accounts[j])
        new_accounts.append(a)
        j += 1
    total = float(str(lira)+"."+str(kurus))
    transfer_amount = (total * 1) / 100
    if new_accounts[source] >= total:
        new_accounts[source] -= (total + transfer_amount)
        new_accounts[destination] += total
        for i in new_accounts:
            new_num = round(i,2)
            str(new_num)
            accounts[k] = new_num
            k += 1
        print(accounts)
    else:
        print(accounts)


