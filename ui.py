from tkinter import *

import quiz_brain
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:


    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.answer = 'True or False'
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text='Score: 0', pady= 20, bg=THEME_COLOR, fg='White')
        self.label.grid(column=1,row=0)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.ques_text = self.canvas.create_text(150,125, text='Amazon acquired', fill= THEME_COLOR, width= 280, font=('Ariel', 20, 'italic'))

        right_image = PhotoImage(file='images/true.png')
        self.button_right = Button(command= self.right, image=right_image, highlightthickness=0)
        self.button_right.grid(column=0, row=2, pady= 50)

        wrong_image = PhotoImage(file='images/false.png')
        self.button_wrong = Button(command= self.wrong, image=wrong_image, highlightthickness=0)
        self.button_wrong.grid(column=1, row=2, pady= 30)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text = q_text)
        else:
            self.canvas.itemconfig(self.ques_text, text="You've reached the end of the quiz")
            self.button_right.config(state='disabled')
            self.button_wrong.config(state='disabled')

    def right(self):
        right = self.quiz.check_answer('True')
        self.give_feedback(right)


    def wrong(self):
        right = self.quiz.check_answer('False')
        self.give_feedback(right)

    def give_feedback(self, right):

        if right:
            self.canvas.config(bg='Green')
        else:
            self.canvas.config(bg='Red')
        self.window.after(1000, self.get_next_question )