import random
import json
import time

def bank_question(quest):
    for i, display_quest in enumerate(quest):
        print(i + 1, "-", display_quest["question"])

#def add_quest():
    #question = input("Add a question: ")
    #options = input("Add options: ")
    #answer = input("The answer to this questions: ")
    #display_quest = {"question" : question, "options" : options, "answer" : answer}
    #return display_quest
#removed this bc I think the "user" shouldnt be the one adding the questions, the questions should be already in the "system"

def delete_quest(questions):
    bank_question(questions)

    while True:
        num = input("enter a number to delete: ")
        try:
            num = int(num)
            if num <= 0 or num > len(questions):
                print("Invalid Number, out of range")
            elif num == "q":
                break
            else:
                print("contact deleted")
                break
        except:
            print("Invalid Number")

    questions.pop(num - 1)


def search_quest(questions):
    print("")
    search_question = input("Question you want to find: ").lower()
    results = []
    for display_quest in questions:
        item = display_quest["question"]
        #choices = display_quest["options"]
        #response = display_quest["answer"]
        #currently remove bc I dont think is a practical way to search for a question
        
        if search_question in item.lower():
            results.append(display_quest)
        else:
            pass
        print("")
    print("Your search found", len(results), "resulsts.")
    if len(results) > 10:
        print("Try to be more specific, in order to find the exact question you are looking for.") 
        print("")
    bank_question(results)

def get_questions():
    with open("question_bank.json", "r") as f:
        questions = json.load(f) ["questions"]
        return questions

def get_random(questions, num_questions):
    if num_questions > len(questions):
        num_questions = len(questions)

    random_questions = random.sample(questions, num_questions)
    return random_questions

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(str(i + 1) + ".", option)

    number = int(input("Enter the number of your answer: "))
    if number < 1 or number > len(question["options"]):
        print("Invalid Number, Wrong Answer")
        return False
    
    correct = question["options"][number - 1] == question["answer"]
    return correct


with open("question_bank.json", "r") as f: #this codes makes pytohn open tje json file. ("name of file", "mode(in this case read)") as f(file)
    questions = json.load(f)["questions"]


print("Hi welcome to your BOQ, Bank of Questions!")
while True:
    print("")
    if len(questions) == 0:
        print("You currently have 0 Questions in your Bank, add more in order to make a quiz!")
    elif len(questions) == 1:
        print("You currently have ", len(questions), "question")
    else:
        print("You currently have ", len(questions), "questions")

    input_command = input("Do you wish to make a quiz, delete a question, search or 'Q' to quit? ").lower()

    if input_command == "delete":
        delete_quest(questions) 
        print("Question Deleted")
        
    elif input_command == "quiz":

        questions = get_questions()
        total_questions = int(input("Enter the number of questions: "))
        random_questions = get_random(questions, total_questions)
        correct = 0
        start_time = time.time()

        for question in random_questions:
            is_correct = ask_question(question)
            if is_correct:
                correct += 1

        print("-----------------")

        completed_time = time.time() - start_time
        print("Summary")
        print("Total Questions:", total_questions)
        print("Correct Answers:", correct)
        print("Score:", str(round((correct / total_questions) * 100, 2)) + "%")
        print("Time:", round(completed_time, 2), "seconds")
        
    elif input_command == "search":
        search_quest(questions)
        
    elif input_command == "q" or input_command == "quit":
        break
    else:
        print("Invalid Command")
        break



with open("question_bank.json", "w") as f: #this codes makes python open the json file. ("name of file", "mode(in this case write)") as f(file)
    json.dump({"questions": questions}, f)    

