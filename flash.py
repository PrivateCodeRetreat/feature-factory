import tkinter as tk
import random

# Step 1: Setup and Dependencies
# Assuming a simple dictionary for Spanish words
spanish_words = {
    "hola": {"translation": "hello", "attempts": 0, "mistakes": 0}, 
    "gracias": {"translation": "thank you", "attempts": 0, "mistakes": 0}, 
    "libro": {"translation": "book", "attempts": 0, "mistakes": 0},
    "perro": {"translation": "dog", "attempts": 0, "mistakes": 0}, 
    "gato": {"translation": "cat", "attempts": 0, "mistakes": 0}, 
    "amor": {"translation": "love", "attempts": 0, "mistakes": 0}
}
# Step 2: Designing the GUI
class SpanishFlashcardsApp:
    def __init__(self, master):
        self.master = master
        master.title("Spanish Flashcards")
        master.geometry("400x300")

        self.current_word = ""
        self.flashcard_label = tk.Label(master, text="", font=("Arial", 24))
        self.flashcard_label.pack(pady=50)

        self.answer_button = tk.Button(master, text="Show Answer", command=self.show_answer)
        self.answer_button.pack()

        self.correct_button = tk.Button(master, text="Correct", command=lambda: self.user_response(True))
        self.correct_button.pack()

        self.incorrect_button = tk.Button(master, text="Incorrect", command=lambda: self.user_response(False))
        self.incorrect_button.pack()

        self.next_flashcard()

    def choose_word(self):
        least_practiced_words = sorted(spanish_words.keys(), key=lambda k: (spanish_words[k].get('attempts', 0), -spanish_words[k].get('mistakes', 0)))
        return least_practiced_words[0]
    
    def next_flashcard(self):
        self.current_word = self.choose_word()
        self.flashcard_label.config(text=self.current_word)
        self.answer_button.config(state="normal")
        self.correct_button.config(state="disabled")
        self.incorrect_button.config(state="disabled")

    def show_answer(self):
        # self.flashcard_label.config(text=spanish_words[self.current_word])
        self.flashcard_label.config(text=spanish_words[self.current_word]["translation"])
        self.answer_button.config(state="disabled")
        self.correct_button.config(state="normal")
        self.incorrect_button.config(state="normal")

    def user_response(self, correct):
        word_data = spanish_words.get(self.current_word, {})
        word_data['attempts'] = word_data.get('attempts', 0) + 1
        if not correct:
            word_data['mistakes'] = word_data.get('mistakes', 0) + 1
        spanish_words[self.current_word] = word_data
        self.next_flashcard()
# Step 3: Running the Application
def main():
    root = tk.Tk()
    app = SpanishFlashcardsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
