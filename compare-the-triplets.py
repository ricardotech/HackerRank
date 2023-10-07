def compareTriplets(a, b):
    alice = 0
    bob = 0
    output = []


    if len(output) == 0:
        if a[0] == b[0]:
            print("igual")
        else:
            if a[0] > b[0]:
                alice = alice + 1
            else:
                print("primeiro ponto, bob + 1")
                bob = bob + 1

        if a[1] == b[1]:
            print("igual")
        else:
            if a[1] > b[1]:
                print("segundo ponto, alice + 1")
                alice = alice + 1
            else:
                bob = bob + 1

        if a[2] == b[2]:
           print("igual")
        else:
            if a[2] > b[2]:
                alice = alice + 1
            else:
                bob = bob + 1
        

        output = [alice, bob]
        return output
                               

a = [17, 28, 30]
b = [99, 16, 8]

result = compareTriplets(a, b)

print(result)