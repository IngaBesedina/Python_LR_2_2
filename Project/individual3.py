#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    sum = 0

    for i in range(21, 100):
        if i % 3 == 0:
            sum += i

    print(sum)
