import csv
from datetime import datetime


def csv_to_dicts(file_path, include_ts=True):
    output = []
    with open(file_path, newline='') as input_file:
        reader = csv.DictReader(input_file, delimiter=",")
        counter = 0
        for row in reader:
            counter += 1
            if include_ts:
                row['UPDATED_TS'] = datetime.now()
                row['INSERTED_TS'] = datetime.now()
            output.append(row)
            if counter % 1000 == 0:
                print("{} records processed".format(counter))
    print('{} records from {}'.format(counter, file_path))
    return output
