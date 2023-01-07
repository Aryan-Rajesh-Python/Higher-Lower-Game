import pyfiglet
import random
from data import data
app=pyfiglet.figlet_format("Higher Lower Game")
print(app)
def get_random():
    return random.choice(data)
def format(account):
    name=account["Name"]
    occupation=account["Occupation"]
    return f"{name}, a {occupation}"
def check_answer(guess,a_followers,b_followers):
    if(a_followers>b_followers):
        return guess=="a"
    elif(a_followers<b_followers):
        return guess=="b"
def game():
    score=0
    a=get_random()
    b=get_random()
    game_continue=True
    while game_continue:
        a=b
        b=get_random()
        while(a==b):
            b=get_random()
        print(f"Compare A: {format(a)}")
        print(f"against B: {format(b)}")
        guess=input("Enter A or B: ").lower()
        a_followers=a["Followers"]
        b_followers=b["Followers"]
        is_correct=check_answer(guess,a_followers,b_followers)
        if is_correct:
            score+=1
            print(f"Your current score: {score}")
        else:
            game_continue=False
            print(f"Your Final Score: {score}")
game()

