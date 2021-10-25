"""Practice programs on list operations"""



L = [14,33,51,18,10,76,55,27,11,91]
i = 0
print("Find below even numbers form list")
while i < len(L):
    if(L[i] % 2 == 0):
        print(L[i])
    i = i + 1

L = [14,33,51,18,10,76,55,27,11,91]
i = 0
print("Find below odd numbers from list")
while i < len(L):
    if(L[i] % 2 != 0):
        print(L[i])
    i = i + 1

