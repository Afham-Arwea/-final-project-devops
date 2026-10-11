import tkinter as tk
import random
from tkinter import messagebox

class GuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number - Qwen Lab")
        self.root.geometry("300x200")
        
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        
        self.label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=5)
        
        self.button = tk.Button(root, text="Submit Guess", command=self.check_guess, bg="blue", fg="white")
        self.button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", font=("Arial", 11))
        self.result_label.pack(pady=5)

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            self.attempts += 1
            
            if user_guess < self.secret_number:
                self.result_label.config(text="Too low! Try again.", fg="orange")
            elif user_guess > self.secret_number:
                self.result_label.config(text="Too high! Try again.", fg="orange")
            else:
                messagebox.showinfo("Victory!", f"Correct! You did it in {self.attempts} attempts.")
                self.secret_number = random.randint(1, 100)
                self.attempts = 0
                self.result_label.config(text="Game Reset! New number generated.", fg="green")
            self.entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessGame(root)
    root.mainloop()
