# To Do list: 
# Generate image depending on the number of questions user wanted in normal mode
# Make infinite mode work
# Make quit button allow start window to stay open when it's clicked
# Print the number of correct and incorrect below the entry box
# Say good job if user input is in the list (of notes)
# Display no. questions answered & remaining
# Check gerenate_image depending on user input (might change image although input is returned false)


from tkinter import *
from functools import partial    # To prevent unwanted windows
import random   


class Start:
  
  def __init__(self, parent):

    # GUI to get starting question and mode
    self.start_frame = Frame(padx=10, pady=10)
    self.start_frame.grid()
    
    # Start up intro (clicking normal or infinite)
    start_intro = Label(self.start_frame, text="Welcome to the quiz of Guess the Note! "
                                    "\nPlease enter the number of questions wanted "
                                    "\n (between 10 and 50) for normal mode. Ignore "
                                    "\nthe input box and click the infinite button "
                                    "\nfor the infinite mode.",
                                      font=("Arial", "11"))
    start_intro.grid(pady=15)

    # Allow user to input the number of questions they want
    self.total_questions = Entry(parent)
    self.total_questions.grid(pady=10)

    # Set total questions as 0
    total_questions = IntVar()
    total_questions.set(0)


    # Display the number of questions wanted in normal mode but not in infinite mode                  
    self.total_question_label = Label(self.start_frame, font="Arial 12 bold", fg="green",
                                text="How many questions do you want: ?", wrap=300,
                                justify=LEFT)
    self.total_question_label.grid(row=4, pady=10)

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
      total_questions = int(self.total_questions.get())

      # Check if user input is between 10 and 50 
      if total_questions not in range(10, 51):
        self.answer.config(text="Out of range. Please enter " 
                                "\nan integer between 10 and 50", 
                                font=("Arial", "12"), fg="red")
        return False
      
      else:
        self.answer.config(text="Okay!", font=("Arial", "12"), fg="green")
        to_infinite = Quiz(total_questions)
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
    def __init__(self, total_questions):

        # GUI Setup
        self.quiz_box = Toplevel()
        
        # If users press at top, quiz quits
        self.quiz_box.protocol('WM_DELETE_WINDOW',self.to_quit)

        self.quiz_frame = Frame(self.quiz_box)
        self.quiz_frame.grid()

      # Display the number of questions wanted in normal mode but not in infinite mode                  
        self.total_question_label = Label(self.quiz_frame, font="Arial 12 bold", fg="green",
                                    text="Total questions: {}".format(total_questions), wrap=300,
                                    justify=LEFT)
        self.total_question_label.grid(row=4, pady=10)

       # Change total_questions number to infinite mode when user input 
        if total_questions not in range(10,50):
          self.total_question_label.config(text="--- Infinite Mode ---")

        else:
          pass

        print(total_questions)

        # initialise variables
        self.correct_ans = StringVar()

        # Set correct and incorrect labels to 0
        self.correct_number = IntVar()
        self.correct_number.set(0)

        # Set question number to 0 and increase by 1 everytime a question is generated
        self.question_number = 0

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
        photo = PhotoImage(file="Programming_images/question_150.gif")

        self.photo1_label = Label(self.qbox_frame, image=photo, padx=10, pady=10)
        self.photo1_label.photo = photo
        self.photo1_label.grid(row=0, column=0)

        # Play button goes here (ro1 3)
        self.play_button = Button(self.quiz_frame, text="Play",
                                  bg="#FFFF33", font="Arial 15 bold", width=20,
                                  padx=10, pady=10, command=self.generate_question)                       

        # bind button to <enter> (users can push enter to reveal the boxes)
        self.play_button.focus()
        self.play_button.bind('<Return>', lambda e: self.generate_question())
        self.play_button.grid(row=3)

        # Help and quiz stats button (row 5)
        self.help_frame = Frame(self.quiz_frame)
        self.help_frame.grid(row=6, pady=10)

        self.help_button = Button(self.help_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  bg="#808080", fg="white", command=self.help)
        self.help_button.grid(row=6)

        # Quit Button
        self.quit_button = Button(self.quiz_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit, justify= LEFT, padx=5, pady=10)
        self.quit_button.grid(row=9, pady=20)

    # Allow quiz window to be dismissed / quit
    def close_quiz(self):
      self.quiz_box.destroy()

    def to_start(self):
      Start()
    
    # Function code reference to Mystery Box project
    # Fix and change variables appropriately
    def generate_question(self):
      
      # Make play button, instruction text and total question text disappear when quiz begins
      self.play_button.destroy()
      self.instructions_label.destroy()
      self.total_question_label.destroy()

      self.generate_image()
    
      # Display question text everytime random image is generated
      self.question_line = Label(self.quiz_frame, text="What is the note below?", font="Arial 14")
      self.question_line.grid(row=1)
      
      self.input_frame = Frame(self.quiz_frame)
      self.input_frame.grid(row=6, pady=10)

      # Entry box for users to enter their answer
      self.answer_input = Entry(self.input_frame)
      self.answer_input.grid(row=4, column=0, padx=5)

      # Create a next button so that when it is pushed, another image randomly generates
      self.next_button = Button(self.input_frame, text="Next",
                                  font="Arial 13 bold",
                                  bg="light blue", fg="black", command=self.check_input, justify=RIGHT)
      self.next_button.grid(row=4, column=1)

      # Make space for message shown about user input
      self.mssg = Label(self.quiz_frame, text='')
      self.mssg.grid(row=7, pady=20)

      # Create new frame for feedbacks
      self.feedback_frame = Frame(self.quiz_frame)
      self.feedback_frame.grid(row=8)

      # Make correct and incorrect label
      self.correct_label = Label(self.feedback_frame, font="Arial 11 bold", text="Correct: 0", justify=LEFT)
      self.correct_label.grid(row=8, column=0, padx=5)

      # Add back incorrect label and ss for testing and trialling






    # When next button is pushed, check if user input is a string and check / compare to answer
    def check_input(self):

      # Create a list for notes
      note = ["c", "d", "e", "f", "g", "a", "b"] 

      # Call user input, set input into lower case, and make it into a variable
      user_answer = self.answer_input.get().lower()
      correct = self.correct_ans.get().lower()

      number_correct = self.correct_number.get()
      

      # if user input is in the list, it is accepted & is valid
      if user_answer in note:

        # Begin checking user answer by comparing it to the original answer - print correct or incorrect
        if user_answer == correct:
          self.mssg.config(text="Correct!", font=("Arial", "12"), fg="green")
          number_correct += 1

          # Reset number_correct when 1 is added
          self.correct_number.set(number_correct)

          
          num_correct_label = "Correct: {}".format(number_correct)
          self.correct_label.config(text=num_correct_label)
          
        else:
          self.mssg.config(text="Incorrect", font=("Arial", "12"), fg="red")
          

        # Generate next question after user answers the question
        self.generate_image()

      # Print error message if user input is not a letter (float or int)
      else:
        self.mssg.config(text="Please enter a letter "
                          "\nof a musical note", font=("Arial", "12"), fg="red")

        return False
      









    # Allow image to be generated randomly
    def generate_image(self):

      images = []

      # Lead not in the list as that is always 0
      octave_list = ["C_150.gif", "D_150.gif", "E_150.gif", "F_150.gif", "G_150.gif", "A_150.gif", "B_150.gif", "C2_150.gif", "D2_150.gif", "E2_150.gif", "F2_150.gif", "G2_150.gif", "A2_150.gif", "B2_150.gif"]

      # Random images in the list is the first and second octave
      octave = random.choice(octave_list)

      question_image = "Programming_images/" + octave
      self.image = PhotoImage(file=question_image)
      self.question_number += 1
      self.correct_ans.set(octave[0])
          
      images.append(self.image)
      photo = images[0]
      
      # Display prizes & edit background...
      self.photo1_label.config(image=photo)
      self.photo1_label.photo = photo

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


# Generqate answer as first letter (example in sandpit)
# store question and answer as string (same as mystery box balance storing)
# Make first, second octave list into one


# Change correct: {} , Incorrect: {} to Correct out of....  (number of questions for normal mode)
# Edit incorrect part.
# End game if user gets incorrect for infinite mode
# change quit button so that it can go back to the start window