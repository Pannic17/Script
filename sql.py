# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def sql_item_single():
    数据库起始ID = 200
    数量 = 10
    作品ID = 1
    开物编号 = "KW00101"
    链上ID = "1ae3ab2d68c4a22b4f7e8c61c824b5ce8490258a3cef75fcc65aa6f30fb6a542_"
    链上起始ID = 1

    表 = "artwork_item_single"

    head = f'insert into {表} (id, artwork_item_id, single_numbering, is_solded, nft_id)'
    print(head)
    print('    VALUES')
    sql_id = 数据库起始ID
    cin_id = 链上起始ID
    art_id = 作品ID
    for index in range(数量):
        hex_id = hex(sql_id).lstrip('0x').upper().zfill(3)
        # print(hex_id)
        number = f'{开物编号}{hex_id}'
        nft_id = f'{链上ID}{cin_id}'
        data = f'({sql_id}, \'{art_id}\', \'{number}\', 0, \'{nft_id}\'),'
        print(data)
        sql_id += 1
        cin_id += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sql_item_single()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
