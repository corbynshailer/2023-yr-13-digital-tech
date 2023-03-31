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

        instructions = "Please choose the correct answer " \
                       "by pressing one of the buttons " \
                       "below if you believe it is correct. "
        self.quiz_instructions = Label(self.quiz_frame,
                                       text=instructions,
                                       wrap=260, width=40,
                                       justify="left")
        self.quiz_instructions.grid(row=1)




if __name__ == "__main__":
    root = Tk()
    root.title("General Knowledge Quiz")
    Quiz()
    root.mainloop()
