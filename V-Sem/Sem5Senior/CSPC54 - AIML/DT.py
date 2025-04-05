import math
import pandas as pd

# Calculate Entropy Given a Particular Division of Data
def entropy(list):
    # calculating total sum
    sum = 0
    for n in list:
        sum += n
    # calculating total entropy
    ent = 0
    for n in list:
        ent += (n/sum) * math.log(sum/n, 2)
    return ent

# Print the given subset of data in proper matrix format
def print_data(fields, data, use_rows, use_cols):
    for j in use_cols:
        print(fields[j], end = "\t")
    print()
    for i in use_rows:
        for j in use_cols:
            print(data[i][j], end = "\t")
        print()

# Discriminator Identifier Function
def get_discriminator(fields, data, use_rows, use_cols):
    return 0

# Classifier Function
def classify(fields, data, use_rows, use_cols, cond):

    if (len(cond) == 0):
        print("Main Data :-")
    else:
        print("Conditions: ", end = "")
    for pair in cond:
        print(pair[0], "=", pair[1], end = ", ")
    print("Data :-")
    print_data(fields, data, use_rows, use_cols)
    print()

    # Check if further classification is required or not
    flag = True
    n = len(fields)

    x = data[use_rows[0]][n-1]
    for i in use_rows:
        if data[i][n-1] != x:
            flag = False
            break
    
    if (flag): # classification complete
        return
    
    d = get_discriminator(fields, data, use_rows, use_cols) # get the discriminator data
    use_cols.remove(d)
    categset = []
    for i in use_rows:
        categset.append(data[i][d])
    categset = sorted(categset)

# Main Function
def main():

    print("Welcome to Python Decission Trees !")
    print()

    csv = pd.read_csv('data.csv')
    fields = list(csv.columns)
    data = csv.to_numpy()

    use_rows = list(range(len(data)))
    use_cols = list(range(len(fields)))

    classify(fields, data, use_rows, use_cols, [])
    
main()