def new_game():
  guesses = []
  question_num = 1
  correct_guesses = 0

  for key in questions:
    print("-------------------")
    print(key)
    for i in options[question_num-1]:
      print(i)
    guess = input("Enter the answer: ").upper()  
    guesses.append(guess)
    correct_guesses += check_answer(questions.get(key),guess)
    question_num +=1
  display_score(correct_guesses,guesses)  
  play_again()

#---------------------------
def display_score(correct_guesses,guesses):
  print()
  print("--------------")
  print("RESULT")
  print("--------------")
  print("Guesses:",end=" ")
  for i in guesses:
    print(i, end=" ")
  print()  
  print("Answer:",end=" ")
  for key in questions:
    print(questions.get(key) , end =" ")
  print()  

  score = int((correct_guesses/len(questions))*100)
  print("Your score is: "+str(score)+"%")



#---------------------------

def check_answer(answer,guess):
  if answer == guess:
    print("CORRECT")
    return 1
  else:
    print("INCORRECT")
    return 0
  

#---------------------------

def play_again():
  response = input("Do you want to continue, yes or no? ").upper()
  if response == 'YES':
    new_game()
  else:
    print("See you later")  



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