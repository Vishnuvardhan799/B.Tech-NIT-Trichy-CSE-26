def PBox(P, str):
    out = ""
    for i in range (len(P)):
        out += str[P[i]]
    return out

def getKeys(P8, P10, key):
    P10key = PBox(P10, key)
    S = PBox([2, 3, 4, 5, 1, 7, 8, 9, 10, 1], P10key)
    S3 = PBox([4, 5, 1, 2, 3, 9, 10, 6, 7, 8], P10key)
    k1 = PBox(P8, S)
    k2 = PBox(P8, S3)
    return [k1, k2]

def main():
    print("Welcome to Python S-DES Algorithm !")

    print("Enter P10 : ", end = "")
    P10 = input().split()
    for i in range(10):
        P10[i] = int(P10[i])

    print("Enter P8 : ", end = "")
    P8 = input().split()
    for i in range(8):
        P8[i] = int(P8[i])

    '''print("Enter IP : ")
    IP = input()
    print("Enter EP : ")
    EP = input()

    S1 = []
    print("Enter the first s-box matrix : ")
    for i in range (4):
        row = []
        for j in range (4):
            row.append(int(input()))
        S1.append(row)
    
    print("\n")

    S2 = []
    print("Enter the second s-box matrix : ")
    for i in range(4):
        row = []
        for j in range(4):
            row.append(int(input()))
        S2.append(row)
    
    print("\n")'''

    print("Enter the plain text : ", end = "")
    PT = input()
    print("Enter the key : ", end = "")
    K = input()

    keys = getKeys(P8, P10, K)
    print("k1 =", keys[0], "and k2 =", keys[1])

main()