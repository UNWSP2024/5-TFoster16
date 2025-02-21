#Timothy Foster, 2/20/25, Math Quiz Program

#Define the function.
def math_quiz():

    #Import the random module.
    import random

    #Get user input for how long the quiz should be.
    num_questions = int(input("How many questions long would you like this math quiz to be?"))
    
    #Start loop.
    for num_questions in range(num_questions):

        #Get two random numbers.
        number_one = random.randint(100, 999)

        number_two = random.randint(100, 999)

        #Calculate the correct answer.
        realAnswer = number_one + number_two
        
        #Get user input for his or her answer.
        userAnswer = int(input(f"{number_one} + {number_two} = ____"))
        
        #See if the answer is correct and print results accordingly.
        if userAnswer == realAnswer:
            print("Good job! Your answer was correct.")
        else:
            print(f"Sorry, your answer was incorrect. The correct answer was {realAnswer}.")

#Call the above function.
math_quiz()
