import csv


def save_to_csv_file(filename, content, option='a'):
    with open(filename, option) as csvfile:
        csv.writer(csvfile).writerows(content)


def value_at_index(row, at, header):
    return row[header.index(at)]


def find_in_file(filename, value, index):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[index] == value:
                return True
    return False


def check_dir(dir_name: str) -> str:
    if dir_name[-1] != '/':
        return dir_name + '/'
    return dir_name
