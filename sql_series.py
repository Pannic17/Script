import random
import string


def loop_gen():
    s = ', '
    p = '\''
    for i in range(2, 100):
        id = i + 1
        name = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        pos = i * 10

        row = f'(' \
              f'{id}{s}' \
              f'{p}{name}{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{pos}{s}' \
              f'0' \
              f'),'
        print(row)


if __name__ == '__main__':
    # cir_sql()
    head = 'insert into artwork_sereis (id, name, introduction, display_img, position, publish_time) VALUES'
    print(head)
    loop_gen()
