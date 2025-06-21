import tkinter as tk
from tkinter import messagebox
import random


choices = {"Stone": 1, "Paper": 0, "Scissor": -1}
reverse_choices = {1: "Stone", 0: "Paper", -1: "Scissor"}


user_score = 0
comp_score = 0

def play(user_choice_text):
    global user_score, comp_score

    user_choice = choices[user_choice_text]
    computer_choice = random.choice(list(choices.values()))

    user_label.config(text=f"You chose: {reverse_choices[user_choice]}")
    comp_label.config(text=f"Computer chose: {reverse_choices[computer_choice]}")

    if user_choice == computer_choice:
        result = "It's a Draw!"
    elif (user_choice == 1 and computer_choice == -1) or \
         (user_choice == 0 and computer_choice == 1) or \
         (user_choice == -1 and computer_choice == 0):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        comp_score += 1

    result_label.config(text=result)
    score_label.config(text=f"Your Score: {user_score}   |   Computer Score: {comp_score}")

# GUI setup
root = tk.Tk()
root.title("Stone Paper Scissor Game")
root.geometry("400x350")
root.resizable(False, False)
root.config(bg="lightblue")

tk.Label(root, text="Stone Paper Scissor", font=("Arial", 18, "bold"), bg="lightblue").pack(pady=10)

btn_frame = tk.Frame(root, bg="lightblue")
btn_frame.pack(pady=20)

for choice in ["Stone", "Paper", "Scissor"]:
    tk.Button(btn_frame, text=choice, width=10, font=("Arial", 12),
              command=lambda c=choice: play(c)).pack(side=tk.LEFT, padx=10)

user_label = tk.Label(root, text="", font=("Arial", 12), bg="lightblue")
user_label.pack(pady=5)

comp_label = tk.Label(root, text="", font=("Arial", 12), bg="lightblue")
comp_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="darkblue", bg="lightblue")
result_label.pack(pady=10)


score_label = tk.Label(root, text="Your Score: 0   |   Computer Score: 0", font=("Arial", 12, "bold"), bg="lightblue", fg="darkgreen")
score_label.pack(pady=10)

root.mainloop()
