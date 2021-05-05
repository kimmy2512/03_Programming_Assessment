from tkinter import *
from functools import partial    # To prevent unwanted windows
import random

class Start:
    def __init__(self, parent):
        # GUI to get starting question and mode
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Mystery Heading (row 0)
        self.guess_note_label = Label(self.start_frame, text="Guess the Note",
                                       font="Arial 19 bold")
        self.guess_note_label.grid(row=1)

        # Entry box... (row 1)
        self.start_number_entry = Entry(self.start_frame, font="Arial 16 bold")

        self.start_number_entry.grid(row=2)

        # Play Button (row 2)
        self.easymode_button = Button(text="Easy",
                                       command=lambda: self.to_quiz(1))
        self.easymode_button.grid(row=2, pady=10)

    def to_quiz(self, mode):
        total_question = self.start_number_entry.get()
        Quiz(self, mode, total_question)

class Quiz:
    def __init__(self, partner, mode, total_question):
        print(mode)
        print(total_question)

        partner.easymode_button.config(state=DISABLED)

        # initialise variables
        self.question = IntVar()

        # Set starting question to amount entered by user at start of quiz
        self.question.set(total_question)

        # GUI setup
        self.quiz_box = Toplevel()
        self.quiz_frame = Frame(self.quiz_box)
        self.quiz_frame.grid()

        # Heading Row
        self.heading_label = Label(self.quiz_frame, text="Quesiton",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # question Label
        self.question_frame = Frame(self.quiz_frame)
        self.question_frame.grid(row=1)

        self.question_label = Label(self.quiz_frame, text="Question...")
        self.question_label.grid(row=2)

        self.play_button = Button(self.quiz_frame, text="Next",
                                  padx=10, pady=10, command=self.generate_questions)
        self.play_button.grid(row=3)

    def generate_questions(self):
        # retrieve the question from the initial function...
        level = self.question.get()

        # Adjust the question (subtract quiz cost and add pay out)
        # For testing purposes, just add 2
        level += 1

        # Set question to adjusted question
        self.question.set(level)

        # Edit label so user can see their question
        self.question_label.configure(text="Question #: {}".format(level))

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Guess the Note")
    something = Start(root)
    root.mainloop()