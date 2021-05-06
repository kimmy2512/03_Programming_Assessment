# Create Help button
# Add in images
# Make exit button

from tkinter import *
import tkinter
from functools import partial  # To prevent unwanted windows

root = Tk()
root.title("Guess the Note")
root.geometry("400x400")


# A function that checks if the user input is an integer
def int_check():
    try:
        int(total_questions.get())

        # Check if user input is between 10 and 50
        if int(total_questions.get()) not in range(10, 50):
            answer.config(text="Out of range. Please enter an integer between 10 and 50")
            return False

        else:
            answer.config(text="Okay!")
            return True

    # Give error message if user input is not an integer between 10 and 50
    except ValueError:
        answer.config(text="Sorry please enter an integer between 10 and 50")


# Give simple instructions to the user
instruction = Label(root, text="Enter a number between 10 and 50")
instruction.pack(pady=20)

# Allow user to input the number of questions they want
total_questions = Entry(root)
total_questions.pack(pady=10)

# Make button to click to next question
next_button = Button(root, text="Next", command=int_check)
next_button.pack(pady=5)

answer = Label(root, text='')
answer.pack(pady=20)


root.mainloop