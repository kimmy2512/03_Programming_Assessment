# To Do list: 
# Make a "Normal" and "infinite" button
# Make new window with a "start" button on the tope left corner
# Create text saying "what is the musical note below?"
# Put blank image in the centre for trialling purposes
# Make an entry box for user input
# Check that user input is appropriate
# Create ok button

from tkinter import *
from functools import partial    # To prevent unwanted windows
import random   


class Start:
  
  def __init__(self, parent):

    # GUI to get starting question and mode
    self.start_frame = Frame(padx=10, pady=10)
    self.start_frame.grid()

    # Guess the Note Heading (row 0)
    self.title = Label(self.start_frame, text="Guess the Note", font="Arial 19 bold")
    self.title.grid(pady=10, padx=10)

    # Give simple instructions to the user
    instruction = Label(parent, text="To start the game, please enter "
                                     "\nthe number of questions you would "
                                     "\nlike to play for. Choose a "
                                      "\nnumber between 10 and 50.",
                                      font=("Arial", "11"))
    instruction.grid(pady=15)

    # Allow user to input the number of questions they want
    self.total_questions = Entry(parent)
    self.total_questions.grid(pady=10)

    # Make button to click to ok question
    ok_button = Button(parent, text="Ok", font=("Arial", "14"), bg="light blue", fg="black", command=self.int_check)
    ok_button.grid(pady=5, padx=5)

    self.answer = Label(parent, text='')
    self.answer.grid(pady=20)

    # Learn Button (row 1)
    self.learn_button = Button(parent, text="Learn", font=("Arial", "14"), bg="light green", fg="black", padx=5, pady=5, command=self.learn)
    self.learn_button.grid(pady=5, padx=15)
  
  # A function that checks if the user input is an integer
  def int_check(self):
    try:
      int(self.total_questions.get())

      # Check if user input is between 10 and 50
      if int(self.total_questions.get()) not in range(10, 50):
        self.answer.config(text="Out of range. Please enter " 
                                "\nan integer between 10 and 50", font=("Arial", "11"), fg="red")
        return False
      
      else:
        self.answer.config(text="Okay!", font=("Arial", "11"), fg="green")
        return True

    # Give error message if user input is not an integer between 10 and 50
    except ValueError:
      self.answer.config(text="Please enter an integer "
                              "\nbetween 10 and 50", font=("Arial", "11"), fg="red")

  # Button that displays appropriate information by a new window
  def learn(self):
    to_learn = Learn(self)

class Learn:
  def __init__(self, partner):

    # Disable learn button
    partner.learn_button.config(state=DISABLED)

    # Sets up child window (ie: learn box)
    self.learn_box = Toplevel()

    # If users press cross at top, closes learn and 'releases' learn button
    self.learn_box.protocol('WM_DELETE_WINDOW', partial(self.close_learn, partner))

    # Set up GUI Frame
    self.learn_frame = Frame(self.learn_box, width=300)
    self.learn_frame.grid()

    # Set up Learn heading (row 0)

    self.how_heading = Label(self.learn_frame, text="Learn",
                              font="Arial 17 bold")
    self.how_heading.grid(row=0)

    learn_text="Information goes here..."

    # Learn text (label, row 1)
    self.learn_text = Label(self.learn_frame, text=learn_text,
                            justify=LEFT, wrap=400, padx=10, pady=10)
    self.learn_text.grid(row=1)

    # Dismiss button (row 2)
    self.dismiss_btn = Button(self.learn_frame, text="Dismiss",
                              width=7, bg="#660000", fg="white",
                              font="Arial 12 bold", command=partial(self.close_learn, partner))
    self.dismiss_btn.grid(pady=5, padx=15)

  def close_learn(self, partner):
      # Put learn button back to normal..
      partner.learn_button.config(state=NORMAL)
      self.learn_box.destroy()

# Continue loop
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Guess the Note")
    s = Start(root)
    root.mainloop()

