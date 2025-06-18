def sports_quiz():
print("Welcome to the sports quiz")  
print("Type the letter corresponidng to your answer (A, B, C, or D).")  


# Questions and options stored as a dictionary 
questions = {
    "1. Who won the FIFA world cup in 2022?": {
        "options":["A. France", "B. Argentina", "C. Brazil", "D. Germany"],
        "answer": "B"
    }
},
"2. Which country has the most olympic gold medals?": { 
    "options": ["A. USA", "B. China", "C. Russia", "D. Germany"],
    "answer": "A"
},
"3. How many players are in one Football team?": {
    "options": ["A. 15", "B. 13", "C. 11", "D. 10"],
    "answer": "C"
},
"4. How many players are on a basketball team on the court?": {
    "options": ["A. 4", "B. 5", "C. 6", "D. 7"],
    "answer": "B"
}



score = 0

for question, q_data in questions.items():
    print(question)
    for option in q_data["options"]:
        print(option)

        user_answer = input("your answer: ").strip().upper()

        if user_answer == q_data["answer"]:
            print("Correct!\n")
            score += 1 
        else:
            print(f"Wrong. The correct answer was {q_data['answer']}.\n")    

print(f"Quiz finished! Your final score is {score}/{len(questions)}.")            