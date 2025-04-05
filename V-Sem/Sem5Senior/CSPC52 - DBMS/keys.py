# GET SUPER KEYS AND CANDIDATE KEYS PROGRAM - CODED BY PRAJWAL

# Perform Bit Masking of one key
def mask(att, key):
    n = 0 # bitmask
    l = len(att)
    for ch in key:
        n += pow(2, l-att.rfind(ch)-1)
    return n

# Get string key of a given bitmask
def demask(att, n):
    str = ""
    op = int(pow(2, len(att)-1)) # bitmask operator
    p = 0 # position of attribute
    while (op > 0):
        if (n & op):
            str += att[p]
        op //= 2
        p += 1
    return str

# Perform Bit Masking of all Functional Dependencies
def bitmask(att, FD):
    FDM = [] # functional dependencies bitmasks
    for dep in FD:
        FDM.append([mask(att, dep[0]), mask(att, dep[1])])
    return FDM

# Get attribute closure of a given key
def closure(att, FDM, n):
    flag = True
    while flag:
        flag = False
        for FD in FDM:
            if (FD[0] & n == FD[0]): # all LHS terms are present
                newn = n | FD[1] # add RHS terms
                if (newn != n): # change has occured
                    n = newn
                    flag = True
    return n

# Check if given key is a superkey or not
def isSuperKey(att, FDM, n):
    n = closure(att, FDM, n)
    l = len(att)
    return (n == pow(2,l)-1)

# Get core attributes of a relation
def getCore(att, FDM):
    l = len(att)

    # 1. Get attributes neither on the left nor right
    one = pow(2,l)-1
    for FD in FDM:
        one = one & ~FD[0]
        one = one & ~FD[1]
    
    # 2. Get attributes only on the left and not on the right
    two = 0
    for FD in FDM:
        two = two | FD[0]
    for FD in FDM:
        two = two & ~FD[1]
    
    # 3. Perform union of one and two
    three = one | two
    return three # core attributes in bitmask format

# Generate permutation
def getPermutation(att, core):
    F = [] # fixed bits
    V = [] # varying bits

    num = core
    p = len(att)-1

    while (p >= 0):
        if (num % 2 == 0): # varying bit
            V.append(len(att)-p-1)
        else: # fixed bit
            F.append(len(att)-p-1)
        num //= 2
        p -= 1
    
    F.reverse() # reverse list
    V.reverse() # reverse list

    return [F, V]

# Permutation Function
def permute(att, num, P):
    mask = 0
    p = len(att)-1
    while (p >= 0):
        mask += int(pow(2, P[p]) * (num % 2))
        num //= 2
        p -= 1
    return mask

# Get keys of a relation
def getKeys(att, FD):
    FDM = bitmask(att, FD)
    core = getCore(att, FDM) # get core attributes

    ck = [] # candidate keys
    sk = [] # super keys

    FV = getPermutation(att, core)
    F = FV[0] # fixed bits
    V = FV[1] # varying bits
    P = F + V # permutation order
    fixed = int((pow(2, len(F))-1) * pow(2, len(V))) # fixed number to keep adding

    vary = []
    lv = pow(2, len(V))
    for var in range(lv):
        vary.append([var, 0, permute(att, fixed+var, P)])
    for var in range(lv):
        vary[var][1] = (vary[var][0] % 2) + vary[var//2][1]
    vary.sort(key=lambda x:(x[1], -x[0])) # sort in lexographic order

    if (isSuperKey(att, FDM, core)): # core attributes form a super key, then it is the only candidate key
        ck.append(core)
        for var in range(lv):
            sk.append(vary[var][2])
        
    else: # core attributes do not form a super key, then there are many candidate keys
        vis = [False] * lv
        for i in range(lv):
            if (vis[i]):
                continue
            if (isSuperKey(att, FDM, vary[i][2])): # candidate key found
                ck.append(vary[i][2])
                for j in range(i, lv):
                    if (vary[i][2] & vary[j][2] == vary[i][2]):
                        vis[j] = True
        for i in range(lv):
            if (vis[i]):
                sk.append(vary[i][2])
    
    return [ck, sk]

# Main Function
def main():

    print("Welcome to Python Keys Calculator !")
    print()

    # Get attributes
    att = input("Enter the attributes in your relation : ")

    # Get number of functional dependencies
    n = int(input("Enter the number of functional dependencies : "))

    print()

    # Get the functional dependencies
    FD = []
    print("Enter functional dependencies as X Y [meaning X -> Y]")
    for i in range(n):
        f = input("FD" + str(i+1) + " : ")
        FD.append(f.split())
    
    print()

    # Get all keys of a relation
    keys = getKeys(att, FD)

    # Print Candidate Keys
    print("Candidate Keys (" + str(len(keys[0])) + ") : ")
    for ck in keys[0]:
        print(demask(att, ck), end = "\t")
    
    print()
    
    # Print Super Keys
    print("Super Keys (" + str(len(keys[1])) + ") : ")
    for sk in keys[1]:
        print(demask(att, sk), end = "\t")
    
    print(end = "\n\n")
    print("Thank you for using Python Keys Calculator. Bye Bye !")

main()