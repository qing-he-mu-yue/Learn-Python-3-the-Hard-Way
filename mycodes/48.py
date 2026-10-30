# 练习 48：高级用户输入

# 书上只给了 convert_number，scan 让自己照着测试写，下面这个是按词典补的。
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']

def scan(sentence):
    result = []

    for word in sentence.split():
        if word in directions:
            result.append(('direction', word))
        elif word in verbs:
            result.append(('verb', word))
        elif word in stop_words:
            result.append(('stop', word))
        elif word in nouns:
            result.append(('noun', word))
        elif convert_number(word) is not None:
            result.append(('number', convert_number(word)))
        else:
            result.append(('error', word))

    return result
