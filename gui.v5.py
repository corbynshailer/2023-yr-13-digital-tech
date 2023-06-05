from tkinter import *

class Quiz:

    def __init__(self):

        button_font = ("Arial", "14")
        button_fg = "#000000"

        self.quiz_frame = Frame(padx=500, pady=0)
        self.quiz_frame.grid()

        self.quiz_heading = Label(self.quiz_frame,
                                  text="General Knowledge Quiz",
                                  font=("Arial", "14", "bold")
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
        self.quiz_entry.grid(row=2, padx=10, pady=10)

        say = "Type above a valid answer"
        self.quiz_say = Label(self.quiz_frame, text=say,
                              fg="#f73636",
                              font=("Arial", "12")
                              )
        self.quiz_say.grid(row=3)

        self.button_frame = Frame(self.quiz_frame)
        self.button_frame.grid(row=4)

        self.submit_button = Button(self.button_frame,
                                   text="Submit",
                                   bg="#00FF00",
                                   fg=button_fg,
                                   font=button_font, width=12)
        self.submit_button.grid(row=0, column=0, padx=4, pady=4)

        self.clear_button = Button(self.button_frame,
                                   text="Clear",
                                   bg="#ff0000",
                                   fg=button_fg,
                                   font=button_font, width=12)
        self.clear_button.grid(row=0, column=1, padx=4, pady=4)

        self.help_button = Button(self.button_frame,
                                   text="Help/info",
                                   bg="#00FFFF",
                                   fg=button_fg,
                                   font=button_font, width=12)
        self.help_button.grid(row=1, column=0, padx=4, pady=4)

        self.history_button = Button(self.button_frame,
                                   text="history/export",
                                   bg="#808080",
                                   fg=button_fg,
                                   font=button_font, width=12,
                                   state=DISABLED)
        self.history_button.grid(row=1, column=1, padx=4, pady=4)


if __name__ == "__main__":
    root = Tk()
    root.title("General Knowledge Quiz")
    Quiz()
    root.mainloop()