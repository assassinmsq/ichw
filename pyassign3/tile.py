"""tile.py: how many ways there are to till the ground.

__author__ = ""Ma Siqi"
__pkuid__  = "1800011760"
__email__  = "1800011760@pku.edu.cn"
"""
import functools


@functools.lru_cache(maxsize=3)
def hpuchuan(dic, begin, a, A):  # 横着铺放
    for i in range(a):
        if dic[begin + i] == 0 and dic[begin + i + A] == 0:
            return True


def spuzhuan(dic, begin, b, A):  # 竖着铺放
    for i in range(b):
        if dic[begin + i] == 0 and dic[begin + i + A] == 0:
            return True


def tile(ans, a, b, alls=[]):  # 铺砖
    A = len(ans)
    B = len(ans[0])
    d = {}
    r = []
    n = -1
    for v in range(B):
        for h in range(A):
            x = v * A + h
            d.update({x: 0})
    if 0 not in [value for value in d.values()]:
        alls.extend([ans[:]])
    else:
        for (key, value) in d.items():
            if hpuchuan(d, key, a, A) is True:
                for i in range(a):
                    d[key + i] = 1
                    d[key + i + A] = 1
                    r.append(i)
                    r.append(i+A)
                r.sort()
                tup = tuple(r)
            n += 1
            ans[n] = tup
            tile(ans, a, b, alls)
            if spuzhuan(d, key, b, A) is True:
                for i in range(b):
                    d[key + i] = 1
                    d[key + i + A] = 1
                    r.append(i)
                    r.append(i+A)
                r.sort()
                tup = tuple(r)
            n += 1
            ans[n] = tup
            tile(ans, a, b, alls)


def test():
    
def main():
    a = input()
    b = input()
    ans = []
    x = input()
    tile(x, a, b, ans)


if __name__ == '__main__':
    main()
