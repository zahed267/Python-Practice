
print("Welcome to the sports quiz")  
print("Type your answer correspoinidng to the question!.")  
score=0

# Questions and answer options
question = ("1. Who won the FIFA world cup in 2022?")

print(question)
user_answer = input("your answer: ").strip().upper()
if  user_answer == "Argentina".upper():
    print("That's correct, well done!")
    score += 1
    print("Nice you've got ", score, " point")
elif user_answer == "":
    print("Not sure?")    
else:
    print("That's incorrect, better luck next time!")  
    print("The answer is Argentina!")  

question = ("2. Which country has the most olympic gold medals?")
print(question)
user_answer = input("your answer: ").strip().upper()    
if  user_answer == "USA":
    print("That's correct, well done!")
    score += 1
    print("Nice you've got ", score, " point")
elif user_answer == "":
    print("Not sure?")  
else:
    print("That's incorrect, better luck next time!")
    print("The answer is USA!")

question = ("3. How many players are in one Football team?")
print(question) 
user_answer = input("your answer: ").strip().upper()   
if  user_answer == "11":
    print("That's correct, well done!")
    score += 1
    print("Nice you've got ", score, " point")
elif user_answer == "":
    print("Not sure?")      
else:
    print("That's incorrect, better luck next time!") 
    print("The answer is 11")

question = ("4. How many players are on a basketball team on the court?")
print(question)
user_answer = input("user answer: ").strip().upper()
if  user_answer == "5":
    print("That's correct, well done!")
    score += 1
    print("Nice you've got ", score, " point")
elif user_answer == "":
    print("Not sure?")      
else:
    print("That's incorrect, better luck next time!") 
    print("The answer is 5")


#for question, q_data in questions.items():
#    print(question)
#    for option in q_data["options"]:
#        print(option)
#
#        user_answer = input("your answer: ").strip().upper()
#
#        if user_answer == q_data["answer"]:
#            print("Correct!\n")
#            score += 1 
#        else:
#            print(f"Wrong. The correct answer was {q_data['answer']}.\n")    
 
print("Quiz finished! Your final score is", score)
print("Thank you for playing the quiz!")            