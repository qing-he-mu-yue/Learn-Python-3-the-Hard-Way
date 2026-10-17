# 练习 14：提示和传递

from sys import argv

script, user_name = argv
# 跑 py 14.py Frank，Frank 就落到 user_name 上。
# prompt 那句是先把提示符存起来，下面三处都拿它用，改一处三处一起变。
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# 三个引号里能直接写多行，{} 照样替换；前头那个 f 漏了，打出来的就是字面上的花括号。
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
