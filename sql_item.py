import random
import string


def loop_gen():
    for i in range(14, 1000):
        s = ', '
        p = '\''
        id = i + 1
        name = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        numbering = "KW"

        row = f'({id}{s}' \
              f'{p}{name}{p}{s}' \
              f'{p}{numbering}{p}{s}' \
              f'1{s}' \
              f'1{s}' \
              f'100{s}' \
              f'0{s}' \
              f'100{s}' \
              f'3{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'1{s}' \
              f'1{s}' \
              f'{p}empty{p}{s}' \
              f'0{s}' \
              f'0{s}' \
              f'0{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'0{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'0{s}' \
              f'0{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}{s}' \
              f'{p}empty{p}' \
              f'),'
        print(row)


if __name__ == '__main__':
    # cir_sql()
    head = 'INSERT INTO `artwork_item` (`id`, `name`, `numbering`, `creator_id`, `brandor_id`, `price`, `saled_amount`, `total_amount`, `is_sold_out`, `display_img`, `display_img2`, `display_img22`, `display_img3`, `display_img32`, `display_img4`, `display_img42`, `display_img5`, `display_img52`, `display_img53`, `three_d_model`, `three_d_model2`, `artwork_series_id`, `artwork_type_id`, `introduction`, `collect_amount`, `like_amount`, `advertise`, `confirm_link`, `hash_value`, `publisher`, `publish_time`, `nft_url`, `chain_cover`, `index_end`, `index_begin`, `init_id`, `img_hash3`, `img_hash2`, `img_hash1`, `model_hash`, `img_cos3`, `img_cos2`, `img_cos1`, `model_cos_url`, `json_cos_url`, `file_hash`, `wide_img`, `share_img`) VALUES'
    print(head)
    loop_gen()
