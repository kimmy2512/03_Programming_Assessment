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
    
    # Start up intro (clicking normal or infinite)
    start_intro = Label(parent, text="Welcome to the quiz of Guess the Note! "
                                    "\nIf you want to play in the Normal mode, "
                                    "\nplease enter a number between 10 and 50 and "
                                    "\n click the Normal button. For the infinity "
                                    "\nmode, ignore the input box and just click the "
                                    "\nInfinite button to go straight to the quiz! ",
                                      font=("Arial", "11"))
    start_intro.grid(pady=15)

    # Allow user to input the number of questions they want
    self.total_questions = Entry(parent)
    self.total_questions.grid(pady=10)

    self.answer = Label(parent, text='')
    self.answer.grid(pady=20)
    
    # Normal button
    self.normal_button = Button(parent, text="Normal", font=("Arial", "14"), bg="yellow", 
                                fg="black", padx=5, pady=5, command=self.int_check)
    self.normal_button.grid(pady=5, padx=10)
    
    # Infinite buttony
    self.infinite = Button(parent, text="Infinite", font=("Arial", "14"), bg="orange", 
                           fg="black", padx=5, pady=5, command=self.to_quiz)
    self.infinite.grid(pady=5, padx=20)
    
    # Learn Button (row 1)
    self.learn_button = Button(parent, text="Learn", font=("Arial", "14"), 
                                bg="light green", fg="black", padx=10, pady=5, 
                                command=self.learn) 
    self.learn_button.grid(pady=10, padx=15)
    
  # A function that checks if the user input is an integer
  def int_check(self): 
    try:
      int(self.total_questions.get())

      # Check if user input is between 10 and 50 
      if int(self.total_questions.get()) not in range(10, 50):
        self.answer.config(text="Out of range. Please enter " 
                                "\nan integer between 10 and 50", 
                                font=("Arial", "12"), fg="red")
        return False
      
      else:
        self.answer.config(text="Okay!", font=("Arial", "12"), fg="green")
        to_infinite = Quiz(self)
        # hide start up window
        root.withdraw()

    # Give error message if user input is not an integer between 10 and 50
    except ValueError:
      self.answer.config(text="Please enter an integer "
                          "\nbetween 10 and 50", font=("Arial", "11"), fg="red")
    
# Button that displays appropriate information by a new window
  def learn(self):
    to_learn = Learn(self)
    
# Infinite button leads directly to quiz window & begin quiz
  def to_quiz(self):
    to_infinite = Quiz(self)
    # hide start up window
    root.withdraw()

# Class code reference to Mystery Box project
class Quiz:
    def __init__(self, starting_balance):
        print(starting_balance)

        # initialise variables
        self.balance = IntVar()
        # Set starting balance to amount entered by user at start of quiz
        self.balance.set(starting_balance)

        # List for holding stats
        self.round_stats_list = []
        self.quiz_stats_list=[starting_balance, starting_balance]

        # GUI Setup
        self.quiz_box = Toplevel()

        # If users press at top, quiz quits
        self.quiz_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.quiz_frame = Frame(self.quiz_box)
        self.quiz_frame.grid()

        # Heading Row
        self.heading_label = Label(self.quiz_frame, text="Guess the Note",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Instructions label
        self.instructions_label = Label(self.quiz_frame, wrap=300, justify=LEFT,
                                        text="Press <Play> to begin the quiz",
                                        font="Arial 10", padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Boxes goes here
        self.qbox_frame = Frame(self.quiz_frame)
        self.qbox_frame.grid(row=2, pady=10)

        # Display with question photo before quiz begins
        photo = PhotoImage(file="question.gif")

        self.prize1_label = Label(self.qbox_frame, image=photo, padx=10, pady=10)
        self.prize1_label.photo = photo
        self.prize1_label.grid(row=0, column=0)

        # Play button goes here (ro1 3)
        self.play_button = Button(self.quiz_frame, text="Play",
                                  bg="#FFFF33", font="Arial 15 bold", width=20,
                                  padx=10, pady=10, command=self.generate_question)                       

        # bind button to <enter> (users can push enter to reveal the boxes)
        self.play_button.focus()
        self.play_button.bind('<Return>', lambda e: self.generate_question())
        self.play_button.grid(row=3)
        
        # Balance label                     
        self.question_no_label = Label(self.quiz_frame, font="Arial 12 bold", fg="green",
                                   text="Total questions: {self.total_questions}", wrap=300,
                                   justify=LEFT)
        self.question_no_label.grid(row=4, pady=10)

        # Help and quiz stats button (row 5)
        self.help_export_frame = Frame(self.quiz_frame)
        self.help_export_frame.grid(row=5, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  bg="#808080", fg="white", command=self.help)
        self.help_button.grid(row=0, column=0, padx=2, pady=10)

        # Quit Button
        self.quit_button = Button(self.quiz_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=6, pady=10)

    # Allow quiz window to be dismissed / quit
    def close_quiz(self):
      self.quiz_box.destroy()
    
    # Function code reference to Mystery Box project
    # Fix and change variables appropriately
    def generate_question(self):

      question_number = 0
      prizes = []
      stats_prizes = []

      # Allows photo to change depending on stakes.
      # Lead not in the list as that is always 0
      first_octave = ["C.gif", "D.gif", "E.gif", "F.gif", "G.gif", "A.gif", "B.gif"]
      second_octave = ["C2.gif", "D2.gif", "E2.gif", "F2.gif", "G2.gif", "A2.gif", "B2.gif"]

      for item in range(0,3):
        prize_num = random.randint(1,10)

        if 0 < prize_num <= 50:
          prize = PhotoImage(file=first_octave)
          question_number += 1
        else:
          prize = PhotoImage(file=second_octave)
          question_number += 1

        prizes.append(prize)

      photo = prizes[0]

      # Display prizes & edit background...
      self.prize1_label.config(image=photo)
      self.prize1_label.photo = photo1

      # Add round results to stats list
      round_summary = "{} | {} | {} - Number of questions: {} \n"\
                                  .format(stats_prizes[0], stats_prizes[1],
                                    stats_prizes[2], question_number)

      self.round_stats_list.append(round_summary)
      self.stats_button.config(state=NORMAL)
      # print(self.round_stats_list)

    # Allow users to quit the quiz
    def to_quit(self):
      # Close window
      root.destroy()
    
    # Root to go to help class
    def help(self):
      get_help = Help(self)

# Display help / rules for users
class Help:
  def __init__(self, partner):

    # Disable help button
    partner.help_button.config(state=DISABLED)

    # Sets up child window (ie: help box)
    self.help_box = Toplevel()

    # If users press cross at top, closes help and 'releases' help button
    self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

    # Set up GUI Frame
    self.help_frame = Frame(self.help_box, width=300)
    self.help_frame.grid()

    # Set up Help heading (row 0)

    self.how_heading = Label(self.help_frame, text="Help / Instructions",
                              font="Arial 14 bold")
    self.how_heading.grid(row=0)

    help_text="Help / Rules goes here..."

    # Help text (label, row 1)
    self.help_text = Label(self.help_frame, text=help_text,
                            justify=LEFT, wrap=400, padx=10, pady=10)
    self.help_text.grid(row=1)

    # Dismiss button (row 2)
    self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                              width=10, bg="#660000", fg="white",
                              font="Arial 15 bold", command=partial(self.close_help, partner))
    self.dismiss_btn.grid(row=3, column=0)

  def close_help(self, partner):
    # Put help button back to normal..
    partner.help_button.config(state=NORMAL)
    self.help_box.destroy()

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

    learn_text=("The staff consists of five lines and four spaces. "
    "\nEach of those lines and spaces represents a "
    "\ndifferent letter, which in turn represents a note. "
    "\nThe notes are named A-G, and the note sequence "
    "\nmoves alphabetically up the staff. "
    "\n"
    "\nSemitones, or half-steps on the keyboard, allow us to "
    "\nwrite with variety of sounds into music. A sharp, denoted "
    "\nby the ♯ symbol, means that note is a semitone (or half "
    "\nstep) higher than the note head to its right on sheet "
    "\nmusic. Conversely, a flat, denoted by a ♭ symbol, "
    "\nmeans the note is a semitone lower than the note "
    "\nhead to its right. "
    "\n"
    "\n* Make sure to use words when indicating semitones. "
    "\nE.g. c flat")

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

# Change the reveal_boxes to generate_questions
# Find images and download for quiz generation
# Change variable names appropriately
# download question.gif