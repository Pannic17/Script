import sys

from matplotlib import pyplot as plt
import csv
import time


def user_chart(month=8, day=31):
    filename = "lib/user_0909_2330.csv"

    data = []
    date = []
    fig_user = []
    fig_real = []
    fig_time = []
    fig_axis = []
    fig_x = []
    real = 0
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            column = 0
            x = 0
            for row in reader:
                if column == 0:
                    header = row
                else:
                    data.append(row)
                    reg_time = time.strptime(row[19], "%Y-%m-%d %H:%M:%S.%f")
                    date.append(reg_time)
                    real += int(row[18])
                    if reg_time.tm_mon < month:
                        pass
                    elif reg_time.tm_mon == month and reg_time.tm_mday < day:
                        pass
                    elif len(fig_user) == 0 \
                            or fig_time[len(fig_user) - 1].tm_hour < reg_time.tm_hour \
                            or fig_time[len(fig_user) - 1].tm_mday < reg_time.tm_mday \
                            or fig_time[len(fig_user) - 1].tm_mon < reg_time.tm_mon:
                        fig_real.append(int(row[18]))
                        fig_user.append(1)
                        fig_time.append(reg_time)
                        fig_axis.append(time.strftime("%H", reg_time))
                        x += 1
                        fig_x.append(x)
                    else:
                        fig_user[len(fig_user) - 1] += 1
                        fig_real[len(fig_user) - 1] += int(row[18])
                column += 1
    except csv.Error as e:
        print("CSV ERROR")
        sys.exit(-1)

    # if header:
    #     print(header)
    #     print("=============================")
    #
    # for row in data:
    #     print(row[0], row[18], row[19])

    index = 0

    fig = plt.figure(figsize=(len(fig_user), max(fig_user)))
    plt.title("user basic::" + str(real))
    plt.xlabel("time")
    plt.ylabel("amount")
    plt.xticks(fig_x, fig_axis)
    plt.bar(fig_x, fig_user, color="black")
    plt.bar(fig_x, fig_real, color="blue")
    for bar in range(len(fig_user)):
        plt.text(bar + 1, fig_user[bar] + 1, fig_user[bar], ha='center', fontsize=20)

    plt.show()
    for i in fig_real:
        print(i)
        print(time.strftime("%m-%d %H:%M", fig_time[index]))
        index += 1


if __name__ == '__main__':
    user_chart(month=9, day=9)
