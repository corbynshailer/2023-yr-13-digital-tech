import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import csv
import random
from fractions import Fraction


class QuizApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Quiz App")
        self.geometry("400x300")

        self.questions = [
            {
                "question":"where questions will go","correct answer": "qwopqe"}
        ]

        random.shuffle(self.questions)  # Randomize the order of questions

        self.current_question = 0
        self.user_answers = []

        self.question_label = tk.Label(self, text="", padx=10, pady=10)
        self.question_label.pack()

        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack(pady=10)

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack(pady=10)

        self.show_question()

        # Bind the Enter key to submit the answer
        self.answer_entry.bind('<Return>', lambda event: self.submit_quiz())

    def show_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=question["question"])
        self.answer_entry.delete(0, tk.END)



if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
