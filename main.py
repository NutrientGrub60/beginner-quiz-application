from questions import questions
import random

def test():
    print("\nWelcome to my History Test :)")
    print("Good Luck")
    score = 0

    random.shuffle(questions)

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        user_answer = input("Your answer (A, B, C, D, E): ").strip().upper()
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nQuiz Over! Your final score is {score}/{len(questions)}.")
    percentage = int(score/len(questions)*100)
    print(f"\nYour score as a percentage is {percentage}%.")
    if percentage <= 50:
        print("Better luck next time!")
    else:
        print("Wow you know some History, congrats!")




if __name__ == "__main__":
    test()