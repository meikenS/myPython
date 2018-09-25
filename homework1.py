import math


def get_surface_ball(r):
    s = 4 * math.pi * pow(r, 2)  # 球的表面积
    return s


def get_volume_ball(r):
    v = 4 / 3 * math.pi * pow(r, 3)  # 球的体积
    return v


def main():
    r = eval(input('请输入半径值:'))
    s1 = get_surface_ball(r)
    v1 = get_volume_ball(r)
    print("球的表面积:", s1, ",球的体积:", v1)


main()
