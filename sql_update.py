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


def update_prize():
    for i in range(4051, 4251):
        row = f'UPDATE artwork_activity_prize_single SET activity_prize_id = 3 WHERE id = {i};'
        print(row)


def update_numbering():
    form = "artwork_activity_prize_single"
    sql_id = 10809
    number = "KW0010"
    for j in range(1800, 2000):
        index = j + 1
        hex_id = hex(index).lstrip('0x').upper().zfill(3)
        single_number = number + str(3)
        sub_no = f'{single_number}{hex_id}'
        row = f'UPDATE `{form}` SET numbering = \'{sub_no}\' WHERE id = {sql_id};'
        sql_id += 1
        print(row)


def update_single_number():
    form = "artwork_item_single"
    sql_id = 10809
    number = "KW00315"


    for j in range(27, 27+30):
        index = j+1
        hex_id = hex(index).lstrip('0x').upper().zfill(3)
        sub_no = f'{number}{hex_id}'
        row = f'UPDATE `{form}` SET single_numbering = \'{sub_no}\' WHERE id = {sql_id};'
        print(row)
        sql_id += 1


    # for i in range(10341, 10391):
    #     row = f'UPDATE artwork_activity_prize_single SET prize_id = 3 WHERE id = {i};'
    #     print(row)


if __name__ == '__main__':
    # loop_rev()
    # update_prize()
    # update_numbering()
    update_single_number()