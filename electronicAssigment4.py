def problem1(list, index):
    if (index < 0 or index > len(list)):
        return (None)
    else:
        j = 0
        for i in list:
            if (j == index):
                return (i)
            j += 1


def problem2(list, index):
    new_array = []
    if (index < 0 or index > len(list)):
        return (list)
    else:
        j = 0
        for i in list:
            if (j == index):
                pass
            else:
                new_array.append(i)
            j += 1
        return (new_array)


def problem3(list, booln):
    if booln == True:
        return sorted(list)
    elif booln == False:
        return sorted(list, reverse=True)



def problem4(list, weight):
    # number = x, weight = w
    i = 1
    result1 = 0
    result2 = 0
    if (len(list) == len(weight)):
        for x,w in zip(list,weight):
            if (i <= len(list)):
                result1 += (x * w)
                result2 += w
            i += 1
        return (result1 / result2)
    else:
        print("Hatalı içerik !")


def problem5(list1, list2):
    common_counter = 0
    for i in list1:
        if (i in list2):
            common_counter += 1
    return (common_counter)


def problem7(accounts, source, lira, kurus):
    new_money = 0
    if(source < 0 and source > len(accounts) - 1):
        return (accounts)
    else:
        money = float(str(lira)+"."+str(kurus))
        new_money = float(accounts[source]) - money
        accounts[source] = str(format(round(new_money,3),".2f"))
        return (accounts)


def problem9 (list):
    i = 0
    j = 0
    new_array = []
    for x in list:
        if (x in new_array):
            return (x)
            break
        new_array.append(x)
    return (None)







