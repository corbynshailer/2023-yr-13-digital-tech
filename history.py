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
                "question": "What has to be broken before you can use it?",
                "correct_answer": "Egg"
            },
            {
                "question": "What is New Zealands national bird?",
                "correct_answer": "Kiwi"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "correct_answer": "Mars"
            },
            {
                "question": "How many elements are in the periodic table?",
                "correct_answer": "118"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "correct_answer": "Japan"
            },
            {
                "question": "Which is the only body part that is fully grown from birth?",
                "correct_answer": "Eyes"
            },
            {
                "question": "Which animal is known as the 'King of the Jungle'?",
                "correct_answer": "Lion"
            },
            {
                "question": "What is the largest organ in the human body?",
                "correct_answer": "Skin"
            },
            {
                "question": "Where did sushi originate?",
                "correct_answer": "Chine"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "correct_answer": "Pacific"
            },
        ]

        random.shuffle(self.questions)  # Randomize the order of questions

        self.current_question = 0
        self.score = 0
        self.user_answers = []

        self.question_label = tk.Label(self, text="", padx=10, pady=10)
        self.question_label.pack()

        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_quiz, bg="green")
        self.submit_button.pack(pady=10)

        self.help_button = tk.Button(self, text="Help", command=self.display_help, bg="#FFFF00")
        self.help_button.pack()

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack(pady=10)


        self.score_label = tk.Label(self, text="Score: 0/0", padx=10)
        self.score_label.pack()

        self.show_question()

        # Bind the Enter key to submit the answer
        self.answer_entry.bind('<Return>', lambda event: self.submit_quiz())

    def show_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=question["question"])
        self.answer_entry.delete(0, tk.END)
        self.score_label.config(text=f"score: {self.score}/{self.current_question}")

    def submit_quiz(self):
        user_answer = self.answer_entry.get()
        correct_answer = self.questions[self.current_question]"correct_answer"]

        self.user_answers.append((self.current_question, user_answer, correct_answer))

        if user_answer.lower() == correct_answer.lower():
            self.score += 1

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_results()

    def show_results(self):
        score_fraction = Fraction(self.score, len(self.questions))
        self.question_label.config(
            text=f"Quiz Finished!\nYour score: {self.score}/{len(self.questions)} ({score_fraction})")
        self.answer_entry.config(state="disabled")
        self.submit_button.config(state="disabled")
        self.help_button.config(state="disabled")


    def display_help(self):
        help_text = "How to Play the Quiz:\n\n"
        help_text += "1. Read the question carefully.\n"
        help_text += "2. Type your answer in the text entry field.\n"
        help_text += "3. Press Enter or click the 'Submit' button to submit your answer.\n"
        help_text += "4. Repeat steps 1-3 for all the questions.\n"
        help_text += "5. Once you have answered all the questions, the quiz will be finished and your score will be displayed.\n"
        help_text += "6. You can click the 'History' button to view your previous answers.\n"
        help_text += "7. Click the 'Export' button to export the statistics of your answers.\n"

        messagebox.showinfo("Quiz Help", help_text)


if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
