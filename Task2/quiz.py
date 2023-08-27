import tkinter as tk
from tkinter import messagebox

class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        root.iconbitmap(r"C:\Users\rituh\OneDrive\Desktop\python projects\codsoft\Codsoft\Task2\ideas_kmg_icon.ico")
        self.root.configure(bg='skyblue') 
        self.questions = [
            {
                "question": "What is the capital of India?",
                "options": ["London", "Delhi", "Paris", "Rome"],
                "correct_answer": 2
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Jupiter", "Venus", "Saturn"],
                "correct_answer": 1
            },
            {
                "question": "Who is known as the ""God of Cricket"" in India?",
                "options": ["Virat Kohli","Rahul Dravid","Sachin Tendulkar","Virender Sehwag"],
                "correct_answer": 3
            },
            {
                "question": "Who leads the executive branch at the state level in India?",
                "options":["Chief Minister","President","Prime Minister","Governor"],
                "correct_answer": 1
            }
                
        ]
        self.current_question = 0
        self.score = 0

        label=tk.Label(root,text='Quiz Game',font='Consolas 25 bold',padx=5,pady=5, width=15,bg='teal',fg='black')
        label.pack()
        
        self.start_button = tk.Button(root, text="Start",pady=5,padx=5,font='times 13 bold',
                                      bg='darkseagreen', command=self.start_quiz)
        self.start_button.pack()

    def start_quiz(self):
        rules = (
                "Welcome to the Quiz Game!\n\n"
                "Game Rules:\n"
                "1. You will be presented with a series of mcq questions.\n"
                "2. Select the correct option for each question.\n"
                "3. Click 'Next' to move to next question.\n"
                "4. final score will be displayed at the end.\n\n"
                "Click 'Start' to begin the quiz."
                )
        messagebox.showinfo("Quiz Rules", rules)
        self.start_button.pack_forget()
        self.display_question()

    def display_question(self):
        question_data = self.questions[self.current_question]
        question_text = question_data["question"]
        options = question_data["options"]
        
        self.question_label = tk.Label(self.root, text=question_text, font=("Helvetica", 16),
                                       bg="skyblue")
        self.question_label.pack(pady=10)

        self.radio_var = tk.IntVar()
        self.radio_var.set(-1)
        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(self.root, text=options[i], variable=self.radio_var, value=i,
                                    font=("Helvetica", 14), bg="skyblue")
            button.pack(pady=2)
            self.option_buttons.append(button)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question,
                                     font=("Helvetica", 14), bg="darkseagreen", fg="black")
        self.next_button.pack(pady=10)
        
    def next_question(self):
        if self.radio_var.get() == -1:
            messagebox.showerror("Error", "Please select an answer.")
        else:
            if self.radio_var.get() + 1 == self.questions[self.current_question]["correct_answer"]:
                self.score += 1
            self.current_question += 1
            if self.current_question < len(self.questions):
                self.question_label.destroy()
                for button in self.option_buttons:
                    button.destroy()
                self.next_button.destroy()
                self.display_question()
            else:
                messagebox.showinfo("Quiz Completed", f"Quiz completed!Final score is: {self.score}/{len(self.questions)}")
                self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Quiz(root)
    root.mainloop()
