import shelve
from pathlib import Path
import pprint
import os
import random


# Here is what the program does:

#     Creates 35 different quizzes
#     Creates 50 multiple-choice questions for each quiz, in random order
#     Provides the correct answer and three random wrong answers for each question, in random order
#     Writes the quizzes to 35 text files
#     Writes the answer keys to 35 text files

# This means the code will need to do the following:

#     Store the states and their capitals in a dictionary
#     Call open(), write(), and close() for the quiz and answer key text files
#     Use random.shuffle() to randomize the order of the questions and multiple-choice options


capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Create a folder to store the files in
folder = Path(Path.cwd() / './35QquizesFolder')
Path.mkdir(folder)  # Only the first time you execute the programe
print(folder)

for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile = open(folder / f'quiznum{quizNum+1}.txt', 'w')
    answerFile = open(folder / f'quiz_answer{quizNum+1}.txt', 'w')

    # Write out the header for the quiz.
    quizFile.write('Name: \nDate: \nPeriod: \n')
    quizFile.write((' ' * 20) + f'State capitales Quiz (From {quizNum+1})')
    quizFile.write('\n\n')

    answerFile.write('\n\n\n' +
                     (' ' * 20) + f'State capitales Quiz Answers (From {quizNum+1})\n\n\n')
    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    #  Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())

        # wrongAnswers now contain all the answers , we need to remove the correct one
        del wrongAnswers[wrongAnswers.index(correctAnswer)]

        # get 3 values from the wrong answers list
        wrongAnswers = random.sample(wrongAnswers, 3)

        # make the opption
        answersOption = wrongAnswers + [correctAnswer]

        # shuffle the aswers option
        random.shuffle(answersOption)

        # Write the question and answer options to the quiz file.
        quizFile.write(
            f'# {questionNum + 1}: What is the capital of {states[questionNum]}? \n')

        ABCD = 'ABCD'
        for i in range(4):
            quizFile.write(f'\t{ABCD[i]} {answersOption[i]}.? \n')

        quizFile.write('\n')

        # Write the answer key to a file.
        answerFile.write(
            f'Question {questionNum} => capital of {states[questionNum]} is {ABCD[answersOption.index(correctAnswer)]} {correctAnswer}')
        answerFile.write('\n\n')

    quizFile.close()
    answerFile.close()
