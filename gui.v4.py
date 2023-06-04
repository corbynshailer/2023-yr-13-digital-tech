from tkinter import *

class Quiz:

    def __init__(self):

        self.quiz_frame = Frame(padx=500, pady=0)
        self.quiz_frame.grid()

        self.quiz_heading = Label(self.quiz_frame,
                                  text="General Knowledge Quiz",
                                  font=("Arial", "18", "bold")
                                  )
        self.quiz_heading.grid(row=0)

        instructions = "Please type your answer within the entry " \
                       "box with your answer if you " \
                       "believe that it is correct",
        self.quiz_instructions = Label(self.quiz_frame,
                                       text=instructions,
                                       wrap=260, width=40,
                                       justify="left")
        self.quiz_instructions.grid(row=1)

        self.quiz_entry = Entry(self.quiz_frame,
                                font=("Arial", "14")
                               )
        self.quiz_entry.grid(row=2, padx=0, pady=0)

        say = "Enter above a valid answer"
        self.quiz_say = Label(self.quiz_frame, text=say,
                              fg="#f73636",
                              font=("Arial", "12")
                              )
        self.quiz_say.grid(row=3)

        self.button_frame = Frame(self.quiz_frame)
        self.button_frame.grid(row=4)

        self.enter_button = Button(self.button_frame,
                                   text="ENTER",
                                   bg="#0000ff",
                                   fg="#FFFFFF",
                                   font="Arial", width=10)
        self.enter_button.grid(row=0, column=0, padx=0, pady=0)

if __name__ == "__main__":
    root = Tk()
    root.title("General Knowledge Quiz")
    Quiz()
    root.mainloop()