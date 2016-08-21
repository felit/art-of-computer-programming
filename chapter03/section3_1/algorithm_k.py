# -*- coding:utf8 -*-

def k1(x):
    y = x / (10 ** 9)
    for i in range(0, y + 1):
        x = k2(x)
        # print 'num = %010d' % x
        print '\'%010d' % x
        # print 'y = %s' % i
    return x


def k2(x):
    z = x / (10 ** 8) % 10
    if z <= 0:
        x = k3(x)
        # print x
    if z <= 1:
        x = k4(x)
        # print x
    if z <= 2:
        x = k5(x)
        # print x
    if z <= 3:
        x = k6(x)
        # print x
    if z <= 4:
        x = k7(x)
        # print x
    if z <= 5:
        x = k8(x)
        # print x
    if z <= 6:
        x = k9(x)
        # print x
    if z <= 7:
        x = k10(x)
        # print x
    if z <= 8:
        x = k11(x)
        # print x
    if z <= 9:
        x = k12(x)
        # print x
    return x


def k3(x):
    """
        确保>=5* 10**9
    """
    num = 5 * 10 ** 9
    if x < num:
        return x + num
    else:
        return x


def k4(x):
    x = x ** 2 / (10 ** 5) % (10 ** 10)
    return x


def k5(x):
    x = (1001001001 * x) % (10 ** 10)
    return x


def k6(x):
    if x < (10 ** 8):
        x = x + 9814055677
    else:
        x = 10 ** 10 - x
    return x


def k7(x):
    x = x % (10 ** 5) * (10 ** 5) + x / (10 ** 5)
    return x


def k8(x):
    return k5(x)


def k9(x):
    result = 0
    for i in range(1, len('%s' % x) + 1):
        n = x % (10 ** i) / (10 ** (i - 1))
        result += ((n - 1) * (10 ** i)) if n != 0 else 0
    return result / 10


def k10(x):
    return (x ** 2 + 9999) if x < 100000 else x - 99999


def k11(x):
    while (x < 10 ** 9):
        l = len('%s' % x)
        # TODO 有问题
        x = 10 ** l + x
    return x


def k12(x):
    x = ((x * (x - 1)) / (10 ** 5)) % (10 ** 10)
    return x


if __name__ == '__main__':
    # k1(6065038420)
    x = 6065038420
    x = 1
    for i in range(1,10000):
        x = k1(x)

    # k1(1)
    # print len('%s' % 6065038420)