import math


def adjust_position(
        input_x, input_y,
        v_left, v_right, v_top, v_bottom,
        r_left, r_right, r_top, r_bottom,
):
    output_x = input_x
    output_y = input_y
    if input_x < r_left:
        output_x = r_left
    elif input_x > r_right:
        output_x = r_right
    if input_y < r_top:
        output_y = r_top
    elif input_y > r_bottom:
        output_y = r_bottom
    r_width = r_right - r_left
    r_height = r_bottom - r_top
    v_width = v_right - v_left
    v_height = v_bottom - v_top
    output_x = v_left + (output_x - r_left) * v_width / r_width
    output_y = v_top + (output_y - r_top) * v_height / r_height
    return output_x, output_y


def adjust_height(input_w, input_h, coefficent, base_height):
    size = math.sqrt(input_w ^ 2 + input_h ^ 2)
    return size * coefficent + base_height