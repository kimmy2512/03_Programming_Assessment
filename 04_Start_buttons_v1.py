# To Do list: 
# Make a "Normal" and "infinite" button
# When normal is chosen, display entry box for number of questions wanted
# when infinite is chosen, head to quiz window
# no window for normal but entry box & normal button
# click normal for int_check & go straight to quiz

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
    
    # Start up intro (clicking normal or infinite)
    start_intro = Label(parent, text="Please choose Normal or Infinite mode. "
                                    "\nIn Normal mode, you can choose the "
                                    "\nnumber of questions that you want between "
                                    "\n10 and 50. In infinite mode, you continue "
                                    "\n the quiz until you get one wrong.",
                                      font=("Arial", "11"))
    start_intro.grid(pady=15)
    
    # Normal button
    self.normal_button = Button(parent, text="Normal", font=("Arial", "14"), bg="yellow", 
                                fg="black", padx=5, pady=5, command=self.normal)
    self.normal_button.grid(pady=5, padx=10)
    
    # Infinite button
    self.infinite = Button(parent, text="Infinite", font=("Arial", "14"), bg="orange", 
                           fg="black", padx=5, pady=5, command=self.infinite)
    self.infinite.grid(pady=5, padx=20)
    
    # Learn Button (row 1)
    self.learn_button = Button(parent, text="Learn", font=("Arial", "14"), 
                                bg="light green", fg="black", padx=5, pady=5, 
                                command=self.learn)
    self.learn_button.grid(pady=10, padx=15)

# Button that displays appropriate information by a new window
  def learn(self):
    to_learn = Learn(self)

# normal button leads to normal class
  def normal(self):
    to_normal = Normal(self)
    
# Infinite button leads directly to quiz window & begin playing game
  def infinite(self):
    to_infinite = Quiz(self)
    
# Bring up new window when "normal" mode is selected.
class Normal:
    def __init__(self, parent):
        
        # Disable normal button
        parent.normal_button.config(state=DISABLED)

        # Sets up child window (ie: normal box)
        self.normal_box = Toplevel()

        # If users press cross at top, closes normal and 'releases' normal button
        self.normal_box.protocol('WM_DELETE_WINDOW', partial(self.close_normal, parent))

        # Set up GUI Frame
        self.normal_frame = Frame(self.normal_box, width=300)
        self.normal_frame.grid()

        # Set up normal heading (row 0)

        self.how_heading = Label(self.normal_frame, text="Normal",
                                font="Arial 17 bold")
        self.how_heading.grid(row=0)
        
        # Disable normal button
        parent.normal_button.config(state=DISABLED)

        # Give simple instructions to the user
        instruction = Label(parent, text="Please enter a number between 10 and 50 " 
                                        "\nfor the number of questions you would "
                                        "\nlike to play.",
                                        font=("Arial", "11"))
        instruction.grid(pady=15)

        # Allow user to input the number of questions they want
        self.total_questions = Entry(parent)
        self.total_questions.grid(pady=10)

        # Make button to click to ok question
        ok_button = Button(parent, text="Ok", font=("Arial", "14"), bg="light blue", 
                           fg="black", command=self.int_check)
        ok_button.grid(pady=5, padx=5)

        self.answer = Label(parent, text='')
        self.answer.grid(pady=20)
        
        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.learn_frame, text="Dismiss",
                                width=7, bg="#660000", fg="white",
                                font="Arial 12 bold", command=partial(self.close_learn, parent))
        self.dismiss_btn.grid(pady=5, padx=15)
    
    # A function that checks if the user input is an integer
    def int_check(self):
        try:
            int(self.total_questions.get())

            # Check if user input is between 10 and 50
            if int(self.total_questions.get()) not in range(10, 50):
                self.answer.config(text="Out of range. Please enter " 
                                        "\nan integer between 10 and 50", 
                                        font=("Arial", "11"), fg="red")
                return False
            
            else:
                self.answer.config(text="Okay!", font=("Arial", "11"), fg="green")
                return True

        # Give error message if user input is not an integer between 10 and 50
        except ValueError:
            self.answer.config(text="Please enter an integer "
                                "\nbetween 10 and 50", font=("Arial", "11"), fg="red")

    def close_normal(self, partner):
      # Put normal button back to normal..
      partner.normal_button.config(state=NORMAL)
      self.normal_box.destroy()
    
# Learn window / class
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
    s = Normal(root)
    root.mainloop()

