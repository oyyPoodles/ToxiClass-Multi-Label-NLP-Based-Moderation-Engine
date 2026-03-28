import csv

try:
    with open('dataset/train.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        train_lines = sum(1 for row in reader)
    print(f"Train size: {train_lines}")
except Exception as e:
    print("Train error:", e)

try:
    with open('dataset/test.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        test_lines = sum(1 for row in reader)
    print(f"Test size: {test_lines}")
except Exception as e:
    print("Test error:", e)
