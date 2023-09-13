questions = ("What is the capital of France?",
             "What is the capital of Germany?",
             "What is the capital of Spain?",
             "What is the capital of Italy?",
             "What is the capital of Portugal?")

options = (("A. Lyon", "B. Paris", "C. Marseille", "D. Toulouse"),
           ("A. Munich", "B. Hambourg", "C. Berlin", "D. Cologne"),
           ("A. Valencia", "B. Barcelona", "C. Madrid", "D. Seville"),
           ("A. Rome", "B. Milan", "C. Naples", "D. Turin"),
           ("A. Coimbra", "B. Porto", "C. Braga", "D. Lisbon"))

answers = ("B", "C", "C", "A", "D")
guesses = []
score = 0
question_number = 0

for question in questions:
    print()
    print(question)
    for option in options[question_number]:
        print(option)

    
    guess = input("Enter answer (A;B;C;D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("Correct!")
    else:
        print(f"Incorrect! The answer was {answers[question_number]}")

    question_number += 1

print()
print(f"You scored {score} out of {len(questions)}.")
print()
print("Your answers:")
for answer in guesses:
    print(answer, end=" ")
print()
print("Correct answers:")
for answer in answers:
    print(answer, end=" ")
print()

