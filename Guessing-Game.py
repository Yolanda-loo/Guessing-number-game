import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")
        self.root.configure(bg="blue")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        # Title Label
        self.title_label = tk.Label(root, text="Guess the Number!", font=("Arial", 16), bg="blue", fg="white")
        self.title_label.pack(pady=10)

        # Entry for Guess
        self.entry_label = tk.Label(root, text="Enter a number (1-100):", font=("Arial", 12), bg="blue", fg="white")
        self.entry_label.pack()

        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack(pady=5)

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit", font=("Arial", 12), command=self.check_guess, bg="white", fg="blue")
        self.submit_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Arial", 12), bg="blue", fg="white")
        self.result_label.pack()

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1
            if guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congrats! You guessed it in {self.attempts} attempts.")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
