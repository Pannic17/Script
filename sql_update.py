def loop_mod():
    single_id = 14
    for i in range(2, 100):
        series_id = i + 1
        for j in range(10):
            single_id += 1
            row = f'UPDATE artwork_item SET artwork_series_id = 1 WHERE id = {single_id};'
            print(row)


def loop_rev():
    # single_id = 500
    for i in range(89000, 98115):
        row = f'UPDATE artwork_item_single SET is_solded = 0 WHERE id = {i};'
        print(row)


if __name__ == '__main__':
    loop_rev()
0