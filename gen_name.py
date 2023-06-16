import os


def gen_name(dir, prefix):
    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file)):
            print("../top/image/train"+file)
