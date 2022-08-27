def loop_gen():
    id = 88214
    for i in range(900, 1000):
        for j in range(1, 100):
            id += 1
            art_id = i + 1
            numbering = "KW"
            sold = 0
            nft_id = "empty"

            row = f'({id}, \'{art_id}\', \'{numbering}\', 0, \'{nft_id}\'),'
            print(row)


if __name__ == '__main__':
    # cir_sql()
    form = "artwork_item_single"
    head = f'insert into {form} (id, artwork_item_id, single_numbering, is_solded, nft_id)'
    print(head)
    print('    VALUES')
    loop_gen()
