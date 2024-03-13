from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.l_score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.l_score.grid(column=1, row=0)

        self.board = Canvas(width=300, height=250, bg="white")
        self.board_text = self.board.create_text(
            150,
            125,
            width=280,
            text="123",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.board.grid(column=0, row=1, columnspan=2, pady=50)

        img_true = PhotoImage(file="./images/true.png")
        self.btn_true = Button(image=img_true, highlightthickness=0, command=self.true_pressed)
        self.btn_true.grid(column=0, row=2)

        img_false = PhotoImage(file="./images/false.png")
        self.btn_false = Button(image=img_false, highlightthickness=0, command=self.false_pressed)
        self.btn_false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.board.config(bg="white")
        if self.quiz.still_has_questions():
            self.l_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.board.itemconfig(self.board_text, text=q_text)
        else:
            self.board.itemconfig(self.board_text, text="You've reached the end of the quiz.")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.board.config(bg="green")
        else:
            self.board.config(bg="red")

        self.window.after(1000, self.get_next_question)

