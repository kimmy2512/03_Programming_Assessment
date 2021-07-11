# To Do list: 
# End game if user gets incorrect for infinite mode
# change quit button so that it can go back to the start window
# Change Correct label into question number label


from tkinter import *
from functools import partial    # To prevent unwanted windows
import random   
import os

class Start:
  
  def __init__(self):

    # GUI to get starting question and mode
    self.start_frame = Frame(padx=10, pady=10)
    self.start_frame.grid()
    
    # Start up intro 
    start_intro = Label(self.start_frame, text="Welcome to Guess the Note! "
    "\n"
                                    "\nWrite the number of questions "
                                    "\nyou want and press <Start> to "
                                    "\nto begin!",
                                      font=("Arial", "11"))
    start_intro.grid(pady=15)

    # Allow user to input the number of questions they want
    self.total_questions = Entry(self.start_frame)
    self.total_questions.grid(row=5, pady=10)

    # Set total questions as 0
    total_questions = IntVar()
    total_questions.set(0)

    # Ask how many questions user want            
    self.total_question_label = Label(self.start_frame, font="Arial 12 bold", fg="green",
                                text="How many questions do you want (between 10 - 50): ?", wrap=300,
                                justify=LEFT)
    self.total_question_label.grid(row=4, pady=10)

    self.answer = Label(self.start_frame, text='')
    self.answer.grid(row=6, pady=20)
    
    # Start button
    self.start_button = Button(self.start_frame, text="Start", font="Cabin 20 bold", bg="yellow", 
                                fg="black", padx=20, pady=10, command=self.int_check)
    self.start_button.grid(pady=5, padx=10)
    
    # Learn Button (row 1)
    self.learn_button = Button(self.start_frame, text="Learn", font=("Arial", "14"), 
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
        to_play = Quiz(total_questions)
        # hide start up window
        root.withdraw()

    # Give error message if user input is not an integer between 10 and 50
    except ValueError:
      self.answer.config(text="Please enter an integer "
                          "\nbetween 10 and 50", font=("Arial", "11"), fg="red")
    
# Button that displays appropriate information by a new window
  def learn(self):
    to_learn = Learn(self)
    
# button leads directly to quiz window & begin quiz
  def to_quiz(self):
    to_play = Quiz(self)
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

      # initialise variables
      self.correct_ans = StringVar()

      # Set initial value of variables
      self.current_number = IntVar()
      self.current_number.set(1)

      self.correct_number = IntVar()
      self.correct_number.set(0)

      self.incorrect_number = IntVar()
      self.incorrect_number.set(0)

      self.limit = IntVar()
      self.limit.set(total_questions)

      # Make stats list
      self.round_stats_list = []

      # quiz stats...
      self.quiz_stats_list=[total_questions, total_questions]
      self.question_input = []

      # Boxes goes here
      self.qbox_frame = Frame(self.quiz_frame, padx=10, pady=10)
      self.qbox_frame.grid(row=2, pady=10)

      # Call variables
      number_question = self.current_number.get()
    
      # Display question text everytime random image is generated
      self.question_line = Label(self.quiz_frame, text="Click <Next> to begin the quiz", font="Arial 12")
      self.question_line.grid(row=1, pady=10)
      
      self.input_frame = Frame(self.quiz_frame)
      self.input_frame.grid(row=6, pady=10)

      # Entry box for users to enter their answer
      self.answer_input = Entry(self.input_frame)
      self.answer_input.grid(row=4, column=0, padx=5)

      # Function code reference to Mystery Box project
      # Make program generate a random image of a musical note
      self.generate_image()

      # Create a next button so that when it is pushed, another image randomly generates
      self.next_button = Button(self.input_frame, text="Next",
                                  font="Arial 14 bold",
                                  bg="light blue", fg="black", command=self.check_input, justify=RIGHT)
      self.next_button.grid(row=4, column=1)

      # Make space for message shown about user input
      self.mssg = Label(self.quiz_frame, text='')
      self.mssg.grid(row=7, pady=20)

      # Create new frame for feedbacks
      self.feedback_frame = Frame(self.quiz_frame)
      self.feedback_frame.grid(row=8)

      # Make current question label
      self.current_label = Label(self.feedback_frame, font="Arial 11 bold", text="Question: 1", justify=LEFT)
      self.current_label.grid(row=8, column=0, padx=5)    

      # Help and quiz stats button (row 5)
      self.help_export_frame = Frame(self.quiz_frame)
      self.help_export_frame.grid(row=9, pady=10)

      self.help_button = Button(self.help_export_frame, text="Help / Rules",
                                font="Arial 15 bold",
                                bg="#808080", fg="white", command=self.help, justify=LEFT)
      self.help_button.grid(row=9, column=0, padx=10)

      # Make game stats button disabled for first try (no games played). Recycled code from mystery box.
      self.stats_button = Button(self.help_export_frame, text="Quiz Stats",
                                  font="Arial 15 bold",
                                  bg="#003366", fg="white", command = self.to_stats, justify=RIGHT)
      self.stats_button.grid(row=9, column=1, padx=10)

      # Disable stats button until end of quiz
      self.stats_button.config(state=DISABLED)

      # Quit Button
      self.quit_button = Button(self.quiz_frame, text="Quit", fg="white",
                                bg="#660000", font="Arial 18 bold", width=18,
                                command=self.to_return, justify= LEFT, padx=5, pady=10)
      self.quit_button.grid(row=10, padx=10, pady=20)
      
    # When next button is pushed, check if user input is a string and check / compare to answer
    def check_input(self):
      
      # Enable stats button
      self.stats_button.config(state=NORMAL)

      # Change the question text when quiz begins
      self.question_line.config(text="What is the note below?")

      # Create a list for notes
      note = ["c", "d", "e", "f", "g", "a", "b"] 

      # Call all user input and variables from another class to create other variables
      user_answer = self.answer_input.get().lower()
      num_correct = self.correct_number.get()
      num_incorrect = self.incorrect_number.get()
      number_question = self.current_number.get()
      correct_answer = self.correct_ans.get().lower()
      user_limit = self.limit.get()

      # if user input is in the list, it is accepted & is valid
      if user_answer in note:

        # Increase question number every correct or incorrect answer
        number_question += 1

        # Reset number_correct when 1 is added
        self.current_number.set(number_question)

        # Set question label
        num_question_label = "Question: {}".format(number_question)
        self.current_label.config(text=num_question_label) 

        # Begin checking user answer by comparing it to the original answer - print correct or incorrect
        if user_answer == correct_answer:
          self.mssg.config(text="Correct!", font=("Arial", "12"), fg="green")
          num_correct += 1
          self.correct_number.set(num_correct)

        # If the number of questions is equal to the number of questions set at the start, go to end quiz
        elif number_question >= user_limit:

          # Disable next button
          self.next_button.config(state=DISABLED)
          self.next_button.config(text="End of\nQuiz!")

          # Change quit button to restart button
          self.quit_button.config(text="Restart", bg="orange", fg="black")
          
        else:
          self.mssg.config(text="Incorrect", font=("Arial", "12"), fg="red")
          num_incorrect += 1
          self.incorrect_number.set(num_incorrect)    

        # Generate next question after user answers the question
        self.generate_image()

      # Change cover image when question number is 1 to begin the quiz. 
      elif number_question == 1:
        number_question += 1
        
        # Reset number_correct when 1 is added
        self.current_number.set(number_question)

        self.generate_image()

      # Print error message if user input is not a letter (float or int)
      else:
        self.mssg.config(text="Please enter a letter "
                          "\nof a musical note", font=("Arial", "12"), fg="red")

        return False

    # Allow image to be generated randomly
    def generate_image(self):
      
      # Make a list
      images = []

      number_question = self.current_number.get()

      # Lead not in the list as that is always 0
      octave_list = ["C_150.gif", "D_150.gif", "E_150.gif", "F_150.gif", "G_150.gif", "A_150.gif", "B_150.gif", "C2_150.gif", "D2_150.gif", "E2_150.gif", "F2_150.gif", "G2_150.gif", "A2_150.gif", "B2_150.gif"]

      # Random images in the list is the first and second octave
      octave = random.choice(octave_list)

      question_image = "Programming_images/" + octave
      photo = PhotoImage(file=question_image)
      self.correct_ans.set(octave[0])

      self.photo1_label = Label(self.qbox_frame, image=photo, padx=10, pady=10)
      self.photo1_label.grid(row=0, column=0)
      
      # Display prizes & edit background...
      self.photo1_label.config(image=photo)
      self.photo1_label.photo = photo

      # Call & make variable from quiz class
      if number_question >= 2:
        # Call & make variable from quiz class
        correct_answer = self.correct_ans.get()
        question_ans_input = self.answer_input.get()

        # Generate quiz summary for game stats if question number is above 1 (during quiz)
        round_summary = "Musical Note: {} | Your answer: {}".format(correct_answer, question_ans_input)

        # Append round summary in round stats list
        self.round_stats_list.append(round_summary)
      
        ## Testing purposes
        print(self.round_stats_list)

    # Allow users to quit the quiz
    def to_quit(self):
      # Close window
      root.destroy()

    # Allow users to restart quiz when button is pushed
    def to_return(self):

      # Destroy main quiz window
      self.quiz_box.destroy()

      # Unwithdraw
      root.deiconify()

    # Root to go to help class
    def help(self):
      get_help = Help(self)

    # Root to go to Quiz stats class
    def to_stats(self):
      total_questions = self.limit.get()
      question_ans_input = self.answer_input.get()
      QuizStats(self, total_questions, question_ans_input)

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
    "\nmoves alphabetically up the staff."
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

  # Close learn window
  def close_learn(self, partner):
      # Put learn button back to normal..
      partner.learn_button.config(state=NORMAL)
      self.learn_box.destroy()

# Create Quiz stats class so that statistics summary of the quiz is given 
class QuizStats:
  def __init__(self, partner, total_questions, question_ans_input):

    # Disable stats button
    partner.stats_button.config(state=DISABLED)

    # Sets up child window (ie: help box)
    self.stats_box = Toplevel()

    # If users press cross at top, closes help and 'releases' help button

    self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

    # Set up stats Frame
    self.stats_frame = Frame(self.stats_box)
    self.stats_frame.grid()

    # Set up Stats heading (row 0)
    self.stats_heading_label = Label(self.stats_frame, text="Quiz Statistics",
                                      font="Arial 19 bold")
    self.stats_heading_label.grid(row=0)

    # To Export <instructions> (row 1)
    self.export_instructions = Label(self.stats_frame, text="Here are your Quiz Statistics."
                          "Please use the Export button to "
                          "access the results of each "
                          "round that you played", wrap=250,
                      font="Arial 10 italic",
                      justify=LEFT, fg="green",
                      padx=10, pady=10)
    self.export_instructions.grid(row=1)

    # Export dismiss frame
    self.export_dismiss_frame = Frame(self.stats_frame)
    self.export_dismiss_frame.grid(row=3, pady=10)

    # Export Button
    self.export_button = Button(self.export_dismiss_frame, text="Export",
                                font="Arial 12 bold",
                                command=lambda: self.export(total_questions))
    self.export_button.grid(row=0, column=0)

    # Dismiss button
    self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                  font="Arial 12 bold",
                                  command=partial(self.close_stats, partner))
    self.dismiss_button.grid(row=0, column=1)

    # Number of total questions frame
    self.details_frame = Frame(self.stats_frame)
    self.details_frame.grid(row=2)

    # # Number of total questions
    self.total_questions_label = Label(self.details_frame,text="Total Questions: {}".format(total_questions), font="Arial 12 bold")
    self.total_questions_label.grid(row=1, column=0, padx=5)

    # # Number of total questions
    self.ans_input_label = Label(self.details_frame,text="".format(question_ans_input), font="Arial 12 bold")
    self.ans_input_label.grid(row=2, column=0, padx=5)

    # Correct questions
    # Incorrect questions
    # Question / answer

  # Function to lead to export class
  def export(self, game_history):
    Export(self, game_history)

  # Allow users to close stats window
  def close_stats(self, partner):
    # Put history button back to normal..
    partner.stats_button.config(state=NORMAL)
    self.stats_box.destroy()

# Make export class so that users can save quiz stats as file
class Export:
  def __init__(self, partner, calc_history):

    background = "#a9ef99"  # Pale green

    # disable export button
    partner.export_button.config(state=DISABLED)

    # Sets up child window (ie: export box)
    self.export_box = Toplevel()

    # If users press cross at top, closes export and 'releases' export button
    self.export_box.protocol('WM_DELETE_WINDOW',
                              partial(self.close_export, partner))

    # Set up GUI Frame
    self.export_frame = Frame(self.export_box, width=300, bg=background)
    self.export_frame.grid()

    # Set up export heading (row 0)
    self.how_heading = Label(self.export_frame,
                              text="Export / Instructions",
                              font="arial 14 bold", bg=background)
    self.how_heading.grid(row=0)

    # Export Instructions (label, row 1)
    self.export_text = Label(self.export_frame, text="Enter a filename "
                                                      "in the box below "
                                                      "and press Save"
                                                      "button to save your"
                                                      "calculation history"
                                                      "to a text file",
                              justify=LEFT, width=40,
                              bg=background, wrap=250)
    self.export_text.grid(row=1)

    # Warning text (label, row 2)
    self.export_text = Label(self.export_frame, text="If the filename "
                                                      "you enter below "
                                                      "already exists, "
                                                      "its contents will "
                                                      "be replaced with "
                                                      "your calculation "
                                                      "history",
                              justify=LEFT, bg="#ffafaf", fg="maroon",
                              font="Arial 10 italic", wrap=225, padx=10,
                              pady=10)
    self.export_text.grid(row=2, pady=10)

    # Filename Entry Box (row 3)
    self.filename_entry = Entry(self.export_frame, width=20,
                                font="Arial 14 bold", justify=CENTER)
    self.filename_entry.grid(row=3, pady=10)

    # Error Message Labels (initially blank, row 4)
    self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                  bg=background)
    self.save_error_label.grid(row=4)

    # Save / Cancel Frame (row 5)
    self.save_cancel_frame = Frame(self.export_frame)
    self.save_cancel_frame.grid(row=5, pady=10)

    # Save and Cancel Buttons (row 0 of save_cancel_frame)
    self.save_button = Button(self.save_cancel_frame, text="Save",
                              command=partial(lambda: self.save_history(partner, calc_history)))
    self.save_button.grid(row=0, column=0)

    self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                command=partial(self.close_export, partner))
    self.cancel_button.grid(row=0, column=1)

  def save_history(self, partner, calc_history):

    # Regular expression to check filename is valid
    valid_char = "[A-Za-z0-9_]"
    has_error = "no"

    filename = self.filename_entry.get()
    print(filename)

    for letter in filename:
      if re.match(valid_char, letter):
        continue

      elif letter == " ":
        problem = "(no spaces allowed)"

      else:
        problem = ("(no {}'s allowed)".format(letter))
        has_error = "yes"
        break

    if filename == "":
      problem = "can't be blank"
      has_error = "yes"

    if has_error == "yes":
      # Display error message
      self.save_error_label.config(text="Invalid filename - {}".format(problem))
      # Change entry box background to pink
      self.filename_entry.config(bg="#ffafaf")
      print()

    else:
      # If there are no errors, generate text file and then close dialogue
      # add .txt suffix!
      filename = filename + ".txt"

      # create file to hold data
      f = open(filename, "w+")

      f.write("Mystery Box\n\n")

      # add new line at end of each item
      for item in calc_history:
        f.write(item + "\n" + "\n")

      # close file
      f.close()

      # close dialogue
      self.close_export(partner)

  def close_export(self, partner):
    # Put export button back to normal...
    partner.export_button.config(state=NORMAL)
    self.export_button.destroy()

    # History Output goes here.. (row 2)

    # Generate string from list of calculations...
    export_string = ""

    # Export / Dismiss Button Frame (row 3)
    self.export_dismiss_frame = Frame(self.export_frame)
    self.export_dismiss_frame.grid(row=3, pady=10)

    # Export Button
    self.export_button = Button(self.export_dismiss_frame, text="Export",
                                font="Arial 12 bold")
    self.export_button.grid(row=0, column=0)

    # Dismiss button
    self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                  font="Arial 12 bold",
                                  command=partial(self.close_export, partner))
    self.dismiss_button.grid(row=0, column=1)

  def close_export(self, partner):
    # Put export button back to normal..
    partner.export_button.config(state=NORMAL)
    self.export_box.destroy()

# Continue loop
# main routine
if __name__ == "__main__":

    root = Tk()
    root.title("Guess the Note")
    s = Start()
    root.mainloop()


# Don't have duplicate images showing
# Make instructions clear
# Clear user input
# Bind next to <enter>
# user input is not correct for the image generated (pushed forward by 1)