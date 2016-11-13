#!/usr/bin/python
# coding: utf-8

#generate 200 activation codes for my apple store app

import random, string

def gene_activation_code(count, length):
    #make sure codes are diffrent
    res = set()
    while len(res) < count:
        res.add(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length)))  # length 控制位数
    return res

if __name__ == "__main__":
    res = gene_activation_code(200, 8)
    # f = open("codes","w")
    # f.write("\n".join(res))
    # f.close()
    print res
