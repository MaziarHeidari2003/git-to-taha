#------------------------
def new_game():
  guesses = []
  correct_guesses = 0 
  question_num = 1

  for key in questions:
    print("#----------------------")
    print(key)
    for i in options[question_num-1]:
      print(i)
    guess = input("Enter A,B,C or D: ").upper()
    guesses.append(guess)  
    correct_guesses += check_answer(questions.get(key),guess)
    question_num +=1  

  display_score(correct_guesses,guesses)  
#------------------------

def check_answer(answer,guess):
  if guess == answer :
    print("CORRECT")
    return 1
  else:
    print("WRONG")
    return 0
  
#------------------------

def display_score(correct_guesses,guesses):
  print("---------------------")
  print("RESULT")
  print("----------------------")
  print("Answers: ",end="")
  for i in questions:
    print(questions.get(i), end=" ")
  print()  
  print("Guesses: ",end="")
  for i in guesses:
    print(i, end=" ")
  print()  

  score = int((correct_guesses/len(questions))* 100)
  print("your score is: "+str(score)+"%")
  
#------------------------

def play_again():
  response = input("Do you want to play again? (yes or no): ")
  if response == "yes":
    return True
  if response == "no":
    return False

#------------------------


questions = {
  "Who created python? ": "A",
  "What year was python created? ": "B",
  "Python is tributed to wich comedi group? ": "C",
  "Is the earth round? ": "A"
}

options = [
  ["A. Ali Daie", "B. Adel Ferdosipoor", "C. Mark Zucjerburg"],
  ["A. 1999", "B. 1991", "C. 2000","D. 2018"],
  ["A. lonely iland","B. smooth", "C. monty python", "D. SNL"],
  ["A. True","B. False", "C. sometimes","D. whats earth?"]
]

new_game()

while play_again():
  new_game()

print("Byeeeeeeeeee")  

