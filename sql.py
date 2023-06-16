# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def sql_item_prize():
    form = "artwork_activity_prize_single"
    amount = 500
    number = "KW00311"
    sql_start = 5531
    chain_start = 761
    art_id = 22
    id_start = 1
    chain_id = "95ff123bfc71b6a0c90233dd3c41a3d921ee70788a4284ceba71f560ad3655f7_"

    head = f'insert into {form} (id, activity_prize_id, prize_id, numbering, is_draw, nft_id)'
    print(head)
    print('    VALUES')

    sql_id = sql_start
    cin_id = chain_start
    for index in range(id_start, id_start+amount):
        sub_id = index
        hex_id = hex(sub_id).lstrip('0x').upper().zfill(3)
        # print(hex_id)
        sub_no = f'{number}{hex_id}'
        nft_id = f'{chain_id}{cin_id}'
        data = f'({sql_id}, \'{art_id}\', \'{art_id}\', \'{sub_no}\', 0, \'{nft_id}\'),'
        print(data)
        sql_id += 1
        cin_id += 1


def sql_item_single(sql_start, chain_start, art_id, amount, number, chain_id):
    # 数据库起始ID = 1
    # 数量 = 60
    # 作品ID = 1
    # 开物编号 = "KW00101"
    # 链上ID = "1ae3ab2d68c4a22b4f7e8c61c824b5ce8490258a3cef75fcc65aa6f30fb6a542_"
    # 链上起始ID = 1

    # 表 = "artwork_item_single"

    form = "artwork_item_single"
    head = f'insert into {form} (id, artwork_item_id, single_numbering, is_solded, nft_id)'
    print(head)
    print('    VALUES')

    sql_id = sql_start
    cin_id = chain_start
    art_id = art_id
    for index in range(amount):
        sub_id = index + 1
        hex_id = hex(sub_id).lstrip('0x').upper().zfill(3)
        # print(hex_id)
        sub_no = f'{number}{hex_id}'
        nft_id = f'{chain_id}{cin_id}'
        data = f'({sql_id}, \'{art_id}\', \'{sub_no}\', 0, \'{nft_id}\'),'
        print(data)
        sql_id += 1
        cin_id += 1


def cir_sql():
    form = "artwork_item_single"
    amount = 20
    base_no = "KW00101"
    sql_start = 10321
    chain_start = 21
    chain_id = "95ff123bfc71b6a0c90233dd3c41a3d921ee70788a4284ceba71f560ad3655f7_"

    head = f'insert into {form} (id, artwork_item_id, single_numbering, is_solded, nft_id)'
    print(head)
    print('    VALUES')

    for index in range(10, 11):
        art_id = index + 1
        number = f'{base_no}{art_id}'
        if art_id != 2:
            sql_item_single(sql_start, chain_start, art_id, amount, number, chain_id)
        sql_start += amount
        chain_start += amount


def price_update():
    for i in range(173, 371):
        row1 = f'UPDATE artwork_activity_prize_single SET is_draw = 1 WHERE id = {i};'
        # row2 = f'UPDATE artwork_activity_prize_single SET activity_prize_id = 3 WHERE id = {i};'
        # print(row1)
        print(row1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # cir_sql()
    # sql_item_prize()
    # price_update()
    sql_item_single(10809, 1478, 26, 30, "KW00315", "384e446dfd51a5964d06946610c95dfbc09a518242d325cba2e32945fa1b61e5_")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
