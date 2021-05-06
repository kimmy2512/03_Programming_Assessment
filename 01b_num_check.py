# Make sure that number is between 10 to 50 for testing purposes

def num_check(low):
    valid = False
    while not valid:
        try:
            response = float(input("Enter a number: "))

            # Print error message if number is below 10 or above 50
            if response < 10:
                print("Please enter a number between 10 to 50")

            elif response > 50:
                print("Please enter a number between 10 to 50")

            else:
                return response

        except ValueError:
            print("Please enter a number")

# Main routine
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

    if self.start_number_entry >= 50:
        print("Sorry enter between 10 - 50 for testing purposes")

    else:
        print("Okay! {} questions :)".format(self.start_number_entry))

    self.start_number_entry.grid(row=2)

    # Play Button (row 2)
    self.easymode_button = Button(text="Easy",
                                  command=lambda: self.to_quiz(1))
    self.easymode_button.grid(row=2, pady=10)
