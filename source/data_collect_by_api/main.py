import csv
import os

os.environ['BEARER_TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAAG7lqgEAAAAAfWsEfLOPLEwi4Akyne76YE4Zk2E%3D05ByMarEbCUZPnOP5jGpfWlMQfdrlfYdKdFFWikUDMatZoPKjs'


if __name__ == "__main__":
    data = {
        'age': 24,
        'name': 'zhangsan',
        'b': False
    }
    with open('test.csv', "a", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=sorted(list(data.keys())))
        writer.writeheader()
        writer.writerow(data)