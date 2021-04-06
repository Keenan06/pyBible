from random import choice

questions = ["Why do we need to brush our teeth:", "Where does our poop go:", "why is running faster than walking:"]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()

print("Oh ok")