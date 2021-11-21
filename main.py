#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/21 0:41
# @Author: Alafun
# @IDE  : PyCharm
# @Ref  :https://blog.csdn.net/qq_35221523/article/details/88705094

class MissionaryCrossRiver:
    """
    传教士与野人过河问题：双方数量都为 n,小船最大可坐 k人，两岸及小船上的传教士数量不能低于野人，否则会被吃掉，求如何安全过河
    """

    def __init__(self, n: int, k: int):
        self.n = n
        self.k = k
        self.count = 0

    def cross_river(self):
        k = self.k
        a = b = self.n
        c = d = 0
        e = f = 0
        # 传教士一次能
        p_max = k - k // 2

        print("    岸边      小船({})       对岸".format(k))
        print("传教士 野人   传教士 野人  传教士 野人")
        print("{} {} <- 0 0  0 0".format(a, b))
        if self.n / k > 2:
            print("船太小了，无解...")
            return
        print("开始过河...")
        while a > 0:
            # 剩下的传教士恰好可以坐满小船
            if a == k and c == 0:
                a -= k
                b += d
                c = k
                d = 0
                self.move(a, b, c, d, e, f)
                break
            # 第一次过河，送些野人过去开船
            if c == 0 and d == 0:
                b -= k - 1
                d += k - 1
                self.move(a, b, c, d, e, f)
                d -= k - 2
                f += k - 2
                self.move(a, b, c, d, e, f)
            if c == 0 and d == 1:
                p1 = a - k
                p2 = b - k
                # 尽量送多点传教士过河
                if p1 <= p_max:
                    a -= p1
                    b -= p2
                    c += p1
                    d += p2
                    self.move(a, b, c, d, e, f)
                    c -= p1
                    d -= p2
                    e += p1
                    f += p2
                    self.move(a, b, c, d, e, f)
                    continue
                temp = f - e
                if temp == 0:
                    temp = 1
                a -= temp
                c += temp
                self.move(a, b, c, d, e, f)
                c -= temp
                e += temp
                self.move(a, b, c, d, e, f)
        # 收尾工作
        c -= k
        d += 1
        e += k
        f -= 1
        self.move(a, b, c, d, e, f)
        b -= k - 1
        d = k
        self.move(a, b, c, d, e, f)
        d = 1
        f += k - 1
        self.move(a, b, c, d, e, f)
        d += b
        b = 0
        self.move(a, b, c, d, e, f)
        f += d
        d = 0
        print(a, b, "  ", c, d, "->", e, f)
        print("回家啦...")

    def move(self, a, b, c, d, e, f):
        self.count += 1
        if self.count % 2 == 0:
            print(a, b, "<-", c, d, "  ", e, f)
        else:
            print(a, b, "  ", c, d, "->", e, f)


if __name__ == "__main__":
    missionary = MissionaryCrossRiver(9, 5)
    missionary.cross_river()

