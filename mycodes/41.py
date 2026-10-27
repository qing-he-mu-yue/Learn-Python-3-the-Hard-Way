# 练习 41：学会说面向对象

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
"class %%%(%%%):":
"Make a class named %%% that is-a %%%.",
"class %%%(object):\n\tdef __init__(self, ***)" :
"class %%% has-a __init__ that takes self and *** params.",
"class %%%(object):\n\tdef ***(self, @@@)":
"class %%% has-a function *** that takes self and @@@ params." ,
"*** = %%%()":
"Set *** to an instance of class %%%.",
"***.***(@@@)":
"From *** get the *** function, call it with params self, @@@.",
"***.*** = '***'":
"From *** get the *** attribute and set it to '***'."
}

# 这节拿一段"代码骨架"，把里面的占位符换成随机单词，让你口头说出这段代码是什么意思。
# 三种占位符各管一样：
#   %%%  → 类名（首字母大写，类名习惯这么写）
#   ***  → 变量名、属性名
#   @@@  → 参数列表（1 到 3 个，随机）
# 先看上面 PHRASES 那张表：左边是骨架，右边是这句骨架该怎么念。

# 命令行带个 english，就变成"先给答案再问你"
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# 单词表是现从网上抓的，断网、或者那个老地址挂了，就卡在 urlopen 这儿不动了。
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    # random.sample(WORDS, n) 是"从词库里不重复地抽 n 个"
    # snippet.count('%%%') 数一下骨架里有几个类名要填，抽几个就够
    # 后面 [w.capitalize() for w in ...] 是列表推导：抽到的词挨个首字母大写，装回一个列表
    class_names = [w.capitalize() for w in
    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    # @@@ 可能有好几处，每处的参数个数还不一样（1 到 3 个随机），所以先攒好一组参数串
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join (
        random.sample(WORDS, param_count)))

    # 这个 for 走两遍：第一遍是你看到的题，第二遍是标准答案，两遍用同一套替换。
    for sentence in snippet, phrase:
        result = sentence[:]   # 复制一份，别把原字符串改掉

        # 替换的第三个参数写 1，意思是"只换第一个遇到的"。
        # 不写这个 1，同一个 %%% 会被一次性全换成同一个词，那就露馅了。
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # 变量名也是这个换法，一处一处来
        for word in other_names:
            result = result.replace("***", word, 1)

        # 参数列表照办，一处一处来
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# 一直出题，直到你按 Ctrl-D（Windows 上是 Ctrl-Z 再回车），抛 EOFError 才跳出去
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
