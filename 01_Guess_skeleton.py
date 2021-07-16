# To Do list:
# Create starup window with button "Quiz"
# Allow a new popup window for to_quiz class
# Have a button called "next question"
# Increase question # by 1 every time button is clicked, display "question: {}"

from tkinter import *
from functools import partial    # To prevent unwanted windows
import random

# Start class recycled from Mystery Box
class Start:
  def __init__(self, parent):
    # GUI to get starting balance and stakes
    self.start_frame = Frame(padx=10, pady=10)
    self.start_frame.grid()

    # Mystery Heading (row 0)
    self.title = Label(self.start_frame, text="Guess the Note",
                                    font="Arial 19 bold")
    self.title.grid(row=1)

    # Set initial amount of questions as 0
    self.start = 0

    # Play Button (row 2)
    self.quiz_button = Button(text="Quiz", command=Quiz)
    self.quiz_button.grid(row=2, pady=10)

# Recycled code from mystery box
class Quiz:
  def __init__(self):

    self.initial_question = IntVar()
    self.initial_question.set(1)

    # GUI setup
    self.quiz_box = Toplevel()
    self.quiz_frame = Frame(self.quiz_box)
    self.quiz_frame.grid()

    # Heading Row
    heading_label = Label(self.quiz_frame, text="Quiz",
                                font="Arial 24 bold", padx=10,
                                pady=10)
    heading_label.grid(row=0)

    # Question Label
    question_frame = Frame(self.quiz_frame)
    question_frame.grid(row=1)

    self.question_label = Label(self.quiz_frame, text="Level: 1", font="Arial 12")
    self.question_label.grid(row=2, pady=10)

    # Button to go to next question
    self.quiz_button = Button(self.quiz_frame, text="Next Question", font="Arial 12 bold", padx=10, pady=10, command=self.add_questions)
    self.quiz_button.grid(row=3, pady=10, padx=10) 

  # Function to add up number of questions
  def add_questions(self):
    question_number = self.initial_question.get()

    # Increase number of questions by 1
    question_number += 1

    # add question_number variable into existing variable
    self.initial_question.set(question_number)

    # Print out & display the number of question
    self.question_label.config(text="Level: {}".format(question_number))


# main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Guess the Note")
  s = Start(root)
  root.mainloop()