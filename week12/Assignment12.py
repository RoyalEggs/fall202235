quiz = [
    {
        "question": "What year was the Bite of-?",
        "choices": [
            "1979",
            "1992",
            "1987"
        ],
        "answer": "1987"
    },
    {
        "question": "Who was William Afton's first murder?",
        "choices": [
            "Elizabeth Afton",
            "Jeremy Fitsgerald",
            "Charlie Emily"
        ],
        "answer": "Charlie Emily"
    },
    {
        "question": "What was the first Fazbear location?",
        "choices": [
            "Fazbear's Family Dinner",
            "Fazbear Frights",
            "Freddy Fazbear's Mega Pizzaplex"
        ],
        "answer": "Fazbear's Family Dinner"
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
        print(f"Nice. You know the lore!")
    else:
        print(f"William Afton is headed towards your location and moving rapidly.")

    print()  # print a blank line for space

print(f"Correct: {correct} of {problemNumber} ({correct * 100 / problemNumber}%)")