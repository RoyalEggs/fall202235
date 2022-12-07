quiz = [
    {
        "question": "Who said The One Piece Is Real?",
        "choices": [
            "Queen Elizabeth 2",
            "Bowser",
            "Luffy D Monkey"
        ],
        "answer": "Queen Elizabeth 2"
    },
    {
        "question": "What color is a carrot?",
        "choices": [
            "Purple",
            "Pumpkin",
            "A carrot"
        ],
        "answer": "A carrot"
    },
    {
        "question": "What is the best Indie Horror game?",
        "choices": [
            "Poppy Playtime",
            "Five Nights at Freddys",
            "Among Us"
        ],
        "answer": "Among Us"
    }
]

problemNumber = 0
correct = 0
for problem in quiz:
    problemNumber += 1
    print(f"Question {problemNumber}: {problem['question']}")

    for choice in problem['choices']:
        print(f" {choice}")
    
    guess = input("Your guess: ")
    if guess == problem['answer' ]:
        correct += 1
        print(f"You are correct son.")
    else:
        print(f"Terrible Job Supership. You effed that one up.")

    print()  # print a blank line for space

print(f"Correct: {correct} of {problemNumber} ({correct * 100 / problemNumber}%)")