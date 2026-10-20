# 练习 23：字符串、字节和字符编码

import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        # 这就是递归：干完一行，把自己再喊一遍去干下一行。但是递归还是别轻易用吧，这玩意一用，计算量直接爆了
        # 什么时候停？line 是空字符串时 if line: 不成立，函数直接返回 None，一层层退回来。
        # 所以递归不是"循环换个写法"，是"剩下的部分还是同一件事"，才敢喊自己。
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    # encode 把字变成 b'...' 那种字节，decode 再变回来。中间那串 \xe6\x97\xa5 才是计算机真正存的东西。
    # errors 决定"碰上编不出来的字怎么办"：
    #   strict（默认）—— 直接报错，程序停在那儿
    #   ignore —— 那个字当没出现过，直接扔
    #   replace —— 换成一个问号
    # 这节先 encode 再 decode，是让你亲眼看见"字 → 字节 → 字"这一趟来回，两个结果打出来看着一样。
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors= errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages , input_encoding, error)
