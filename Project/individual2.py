#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    x = int(input("Value of x: "))
    y = int(input("Value of y: "))

    if x**2*y > x*y**2:
        max = x**2*y
    else:
        max = x*y**2

    if x - y < x + 2*y:
        min = x - y
    else:
        min = x + 2*y

    U = max**2 + min**2

    print(U)
