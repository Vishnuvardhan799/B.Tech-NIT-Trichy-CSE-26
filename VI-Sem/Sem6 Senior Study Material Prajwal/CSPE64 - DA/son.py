from collections import defaultdict
import itertools
import time
import csv

class MapReduce:
    def __init__(self):
        self.intermediate = defaultdict(list)
        self.result = []

    def emit_intermediate(self, key, value):
        self.intermediate[key].append(value)

    def emit_result(self, value):
        self.result.append(value)

    def execute(self, data, mapper, reducer):
        for record in data:
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

class SonAlgorithm(MapReduce):
    def __init__(self, transactions, support_threshold):
        super().__init__()
        self.transactions = transactions
        self.support_threshold = support_threshold

    def mapper(self, record):
        transaction_id, items = record
        for item in items:
            self.emit_intermediate(item, transaction_id)
        # Generate combinations of items and emit
        for combo in itertools.combinations(items, 2):
            self.emit_intermediate(','.join(combo), transaction_id)

    def reducer(self, item, transaction_ids):
        transaction_count = len(set(transaction_ids))
        if transaction_count >= self.support_threshold:
            self.emit_result((item, transaction_count))

def generate_transactions(data):
    transactions = []
    for idx, transaction in enumerate(data):
        transactions.append((idx, transaction.split()))
    return transactions

if __name__ == "__main__":
    # Example dataset

    text_file = open("basket.csv", 'r')
    data = text_file.read().split('\n')
    transactions = generate_transactions(data)

    support_threshold = 3  # Set the support threshold

    # Start time tracking
    start_time = time.time()

    # Initialize and execute the -Son Algorithm
    algorithm = SonAlgorithm(transactions, support_threshold)
    algorithm.execute(transactions, algorithm.mapper, algorithm.reducer)

    time.sleep(0.5)

    # End time tracking
    end_time = time.time()

    # Output the frequent itemsets
    print("Frequent Itemsets:")
    for item, count in algorithm.result:
        print(f"{item}: {count}")

    # Calculate and output the time taken
    time_taken = end_time - start_time
    print("Time taken:", time_taken, "seconds")