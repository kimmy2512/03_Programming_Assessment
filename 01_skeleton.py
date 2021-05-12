# To do list:
# Make Box label for start window
# Give instructions
# Make box for users to enter how many number of questions they want
# Check user input (validate user entry as number)
# Make button (easy only for testing purposes) to give comment on another / separate window

from tkinter import *
from functools import partial    # To prevent unwanted windows
import random

class Start:
  def __init__(self, partner):
    # GUI to get starting question and mode
    self.start_frame = Frame(padx=10, pady=10)
    self.start_frame.grid()

    # Mystery Heading (row 0)
    self.guess_note_label = Label(partner, self.start_frame, text="Guess the Note",
                                    font="Arial 19 bold")
    self.guess_note_label.grid(row=1)




    # Entry box... (row 1)
    self.start_number_entry = Entry(partner, self.start_frame, font="Arial 16 bold", command=num_check)

    self.start_number_entry.grid(row=2)

    # Play Button (row 2)
    self.easymode_button = Button(partner, text="Easy",
                                    command=lambda: self.to_quiz(1))
    self.easymode_button.grid(row=2, pady=10)
  
    answer = Label(partner, text = '')
    answer.pack(pady=20)
    

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Guess the Note")
    something = Start(root)
    root.mainloop()