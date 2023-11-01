from tkinter import * 
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        ###Label
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        ###Canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="",
                                                     fill=THEME_COLOR,
                                                     font=FONT)

        #Buttons x2
        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.click_true)
        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.click_false)

        #Layout
        self.score.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.right_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def enable_buttons(self):
        self.right_button.config(state="active")
        self.wrong_button.config(state="active")

    def disable_buttons(self):
        self.right_button.config(state="disabled")
        self.wrong_button.config(state="disabled")

    def get_next_question(self):
        self.canvas.configure(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.enable_buttons()
        else:
            self.canvas.itemconfig(self.question_text,
                                   text="You've reached the end of the test")
            self.disable_buttons()

    def click_true(self):
        self.disable_buttons()
        self.give_feedback(self.quiz.check_answer("True"))

    def click_false(self):
        self.disable_buttons()
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.timer = self.window.after(1000, self.get_next_question)
