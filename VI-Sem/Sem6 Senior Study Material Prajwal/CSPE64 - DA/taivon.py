import random
import time
import csv

def generate_negative_border(item_set, frequent_item_sets):
    negative_border = set()
    for item in item_set:
        for transaction in frequent_item_sets:
            if item in transaction and tuple(item_set - {item}) in frequent_item_sets:
                negative_border.add(item)
    return negative_border

def toivonen_algorithm(transactions, min_support, sample_size):
    start_time = time.time()
    n = len(transactions)
    sample = random.sample(transactions, sample_size)
    frequent_item_sets = []
    negative_border = set()

    # Initial pass to find frequent item sets in the sample
    item_counts = {}
    for transaction in sample:
        for item in transaction:
            item_counts[item] = item_counts.get(item, 0) + 1
    frequent_item_sets = [frozenset([item]) for item, count in item_counts.items() if count >= min_support]

    while True:
        candidates = set()
        # Generate candidate item sets
        for item_set1 in frequent_item_sets:
            for item_set2 in frequent_item_sets:
                if len(item_set1.union(item_set2)) == len(item_set1) + 1:
                    candidates.add(item_set1.union(item_set2))

        # Verify candidates against the entire dataset
        for candidate in candidates.copy():
            candidate_support = sum(1 for transaction in transactions if candidate.issubset(transaction))
            if candidate_support >= min_support:
                frequent_item_sets.append(candidate)
            else:
                negative_border.update(generate_negative_border(candidate, frequent_item_sets))

        # Refine the sample if necessary
        if negative_border:
            additional_transactions = [transaction for transaction in transactions if negative_border.intersection(transaction)]
            sample.extend(additional_transactions)
            negative_border.clear()
        else:
            break

    time.sleep(0.005)

    end_time = time.time()
    execution_time = end_time - start_time
    return frequent_item_sets, execution_time

# Example usage
# transactions = [
#     {'apple', 'banana', 'orange'},
#     {'apple', 'banana'},
#     {'apple', 'orange'},
#     {'banana', 'orange'},
#     {'apple', 'banana', 'orange', 'grape'},
#     {'apple', 'grape'},
#     {'apple', 'banana', 'grape'},
#     {'grape'}
# ]
# transactions = [
#     {1, 2, 3},
#     {1, 2},
#     {1, 3},
#     {1, 3, 4},
#     {6, 5, 3}
# ] 

with open('basket.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    transactions = list(csv_reader)
min_support = 2
sample_size = 3

frequent_item_sets, execution_time = toivonen_algorithm(transactions, min_support, sample_size)
print("Frequent Item Sets:", frequent_item_sets)
print("Execution Time:", execution_time, "seconds")