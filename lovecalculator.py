your_name=input("Enter your name:")
partner_name=input("Enter your partner name:")
name=your_name+partner_name
name=name.lower()
t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
true=t+r+u+e
l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")
love=l+o+v+e
love_score=int(str(true)+str(love))
if love_score<10 or love_score>90:
    print(f"Your score is {love_score} and you go together like coke and mentos")
elif love_score>=40 and love_score<=50:
    print(f"Your score is {love_score} and you are alright together")
else:
    print(f"Your love_score is {love_score}%")
