  

"""
 to begin with, i wanted to make the code as efficient as possible
 as it requires 10 question, so i did the following;
 make a dictionary that serves as the question key which has the question
 and answer to the respective question.

 given the question key, i make a new function that i can call which will
 narrate the question, and also store the correct answer.

 the keys in the dictionary serves as the country to be asked
 the values within the given keys are the answers, which are the capitals

 the answers are all lowercase, this is due to me enforcing .lower()
 on user input, so that it is not case-sensitive
"""

question_key = {
    "France": "paris",
    "UAE": "abu dhabi",
    "Georgia": "tbilisi",
    "Spain": "madrid",
    "Poland": "warsaw",
    "Netherlands": "amsterdam",
    "Russia": "moscow",
    "United Kingdom": "london",
    "Norway": "oslo",
    "Turkey": "ankara",
}


# here is the function that i made for answering and checking the questions that is called in the loop
def answer_block(question, answer):
    while True: #i make use of a while loop in order for the user to repeat the question until its correct.
        guess = input(f"What is the capital of {question}?: ") #again, i make use of the f-string function for the print, calling the question as per the iteration in the loop
        guess = guess.lower() #in order to solve case-sensitivity, i enforce the guess to be lowercase, matching the if conditions which looks for an all lower-case input.
        
        if guess == answer:
            print("Correct")
            break
        else:
            print("Incorrect, try again")

"""
 for each key-value pair within the dictionary 'question_key',
 i take the question and answer values and input it into the function i made above,
 it efficiently goes through all the questions given in the list, and 
 takes the correct answer for each question

 within the loop, q represents the question (the 1st key in the dictionary),
 and a represents the answer (the 2nd key in the dictionary)
 passing those two values into the answer_block function gives us the question and answer
 for each question in order
"""
for q, a in question_key.items():
    answer_block(q,a)

