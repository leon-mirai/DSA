


def reverse(mystr):
    # if (isinstance(mystr, str) or len(mystr) < 2 or not mystr ):
    #     return
    arr = []
    
    for i in range(len(mystr) - 1, 0, -1):
        arr.append(mystr[i])

    return ' '.join(arr)


s = "iserdnA si eman vM iH"    

print(reverse(s))


