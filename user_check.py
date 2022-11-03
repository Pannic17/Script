import csv
import sys


def user_check():
    filename = "lib/user_basic_0909.csv"

    user = {}
    dup_user = {}
    count = 0

    try:
        with open(filename, encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[3] in user:
                    user[row[3]].append(row[0])
                    dup_user[row[3]] = user[row[3]]
                    count += 1
                elif len(row[3]) > 0:
                    user[row[3]] = [row[0]]

        print(dup_user)
        print(len(user))
        print(len(dup_user))
        print(len(dup_user)+count)
    except csv.Error as e:
        print("CSV ERROR")
        sys.exit(-1)


if __name__ == '__main__':
    user_check()
