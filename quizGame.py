questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language are we learning?",
        "options": ["A. Java", "B. C++", "C. Python", "D. HTML"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. def", "C. func", "D. create"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. int", "B. str", "C. bool", "D. list"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    }
]

score = 0

print("================================")
print("          PYTHON QUIZ")
print("================================")

for number, question in enumerate(questions, start=1):

    print(f"\nQuestion {number}:")
    print(question["question"])

    for option in question["options"]:
        print(option)

    answer = input("Your answer: ").upper()

    if answer == question["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")
        print("Correct answer:", question["answer"])

print("\n================================")
print("          QUIZ COMPLETE")
print("================================")

print(f"Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100

print(f"Percentage: {percentage:.1f}%")