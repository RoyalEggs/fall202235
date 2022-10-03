score=0
answer= input("what color is the sky")
if answer == "blue":
    score=score + 1
    print("Yes!")
else:
    print("I was looking for 'blue'")
answer= input("How old is the president?")
if answer== "79":
    print("Good.")
    score= score+1
else:
    print("Nope.")
answer= input("How many Great Lakes are there?")
if answer == "5":
    score= score+1
    print("Oh, you are smart!")
else:
    print("Nice try.")
print("Your score is", score)