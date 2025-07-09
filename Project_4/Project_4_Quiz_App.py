import tkinter as tk
from tkinter import messagebox
import json

# Load questions from JSON file
with open("questions.json", "r") as f:
    questions = json.load(f)

current_q = 0
selected_answers = [None] * len(questions)

# Load question into GUI
def load_question(index):
    q = questions[index]
    question_label.config(text=f"Q{index + 1}: {q['question']}")
    selected_option.set(selected_answers[index] if selected_answers[index] else "")
    
    for i in range(4):
        option_buttons[i].config(text=q["options"][i], value=q["options"][i])

# Navigation
def next_question():
    global current_q
    selected_answers[current_q] = selected_option.get()
    if current_q < len(questions) - 1:
        current_q += 1
        load_question(current_q)

def prev_question():
    global current_q
    selected_answers[current_q] = selected_option.get()
    if current_q > 0:
        current_q -= 1
        load_question(current_q)

# On submit: close quiz and show score
def submit_quiz():
    selected_answers[current_q] = selected_option.get()
    score = sum(1 for i, q in enumerate(questions) if selected_answers[i] == q["answer"])
    root.destroy()
    show_result(score)

# Result popup window
def show_result(score):
    result_win = tk.Tk()
    result_win.title("Quiz Result")
    result_win.geometry("400x250")
    result_win.configure(bg="#f0f0f0")

    label = tk.Label(result_win, text=" Quiz Completed! ", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
    label.pack(pady=20)

    score_label = tk.Label(result_win, text=f"Your Score: {score}/{len(questions)}", font=("Arial", 14), bg="#f0f0f0", fg="Green")
    score_label.pack(pady=10)

    exit_btn = tk.Button(result_win, text="Exit", command=result_win.destroy, bg="red", fg="white")
    exit_btn.pack(pady=20)

    result_win.mainloop()

# GUI Setup
root = tk.Tk()
root.title("Quiz App")
root.geometry("500x400")

question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=450, justify="left")
question_label.pack(pady=20)

selected_option = tk.StringVar()

option_buttons = []
for i in range(4):
    btn = tk.Radiobutton(root, text="", variable=selected_option,
                         value="", font=("Arial", 12), anchor="w", justify="left")
    btn.pack(fill="x", padx=20, pady=5)
    option_buttons.append(btn)

nav_frame = tk.Frame(root)
nav_frame.pack(pady=20)

prev_btn = tk.Button(nav_frame, text="Previous", command=prev_question)
prev_btn.grid(row=0, column=0, padx=10)

next_btn = tk.Button(nav_frame, text="Next", command=next_question)
next_btn.grid(row=0, column=1, padx=10)

submit_btn = tk.Button(root, text="Submit Quiz", command=submit_quiz, bg="green", fg="white")
submit_btn.pack(pady=10)

# Start with first question
load_question(current_q)
root.mainloop()
