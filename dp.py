def dp():
    percent = 0.2
    kw_amount = [500, 2000, 1000, 2000, 2000, 800, 2000]
    kw_price = [158, 68, 88, 30, 88, 128, 68]

    total = 0
    index = 0
    for i in range(len(kw_amount)):
        total += kw_price[index] * kw_amount[index] * (1 - percent)
    print(total)
    print(total / 50)


if __name__ == '__main__':
    dp()
