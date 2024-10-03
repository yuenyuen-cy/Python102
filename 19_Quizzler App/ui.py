from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20,pady=20)

        self.score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250,bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="quiz",
            fill=THEME_COLOR,
            font=("Arial",20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img,
                                  highlightthickness=0,
                                  relief="flat", bg=THEME_COLOR,
                                  pady=50,
                                  command=self.select_true
                                  )

        self.false_button = Button(image=false_img,
                                   highlightthickness=0,
                                   relief="flat",
                                   bg=THEME_COLOR,
                                   pady=50,
                                   command=self.select_false
                                   )

        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def select_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def select_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.question_number < len(self.quiz.question_list):
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text=f"You have completed the quiz. Your final score is: {self.quiz.score} / 10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.score.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)


