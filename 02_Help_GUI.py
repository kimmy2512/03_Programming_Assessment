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

# Help Button (row 1)
help_button = Button(root, text="Help",
                     font=("Arial", "14"),
                     padx=10, pady=10, command=help)
help_button.pack(pady=30)


def help():
    print("You asked for help")
    get_help = Help()
    get_help.help_text.configure(text="Help text goes here")


background = "orange"

# disable help button
partner.help_button.config(state=DISABLED)

# Sets up child window (ie: help box)
help_box = Toplevel()

# If users press cross at top, closes help and 'releases' help button
help_box.protocol('WM_DELETE_WINDOW', partial(close_help, partner))

# Set up GUI frame
help_frame = Frame(help_box, width=300, bg=background)
help_frame.grid()

# Set up Help heading (row 0)
how_heading = Label(help_frame, text="Help / Instructions", font="arial 14 bold", bg=background)
how_heading.grid(row=0)

# Help text (label, row 1)
help_text = Label(help_frame, text="",
                  justify=LEFT, width=40, bg=background, wrap=250)
help_text.grid(row=1)

# Dismiss button (row 2)
dismiss_btn = Button(help_frame, text="Dismiss",
                     width=10, bg="orange", font="arial 10 bold",
                     command=partial(close_help, partner))
dismiss_btn.grid(row=2, pady=10)


def close_help(partner):
    # Put help button back to normal...
    partner.help_button.config(state=NORMAL)
    help_box.destroy()


# Continue loop
root.mainloop()