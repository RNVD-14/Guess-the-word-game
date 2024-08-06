from tkinter import *
from random import *
from tkinter import messagebox
import time


def main():
    def back():
        my_window.destroy()
        import index
        index.start_main_page()
    def display_instructions():
        instructions_window = Toplevel(my_window)
        instructions_window.title("Instructions")

        instructions_text = """
        Welcome to the Guess the Word Game!

        Instructions:
        - Click the 'Start' button to begin the game.
        - Choose a category from the options provided.
        - A word will be shown with its jumbled form.
        - Unscramble the word and type your answer in the input field.
        - Click the 'Submit' button to check your answer.
        - You can also click the 'Change Word' button to get a new word.
        - If you're stuck, click the 'Answer' button to reveal the answer (requires points).
        - Try to score as many points as possible!

        Have fun playing!
        """

        instructions_label = Label(
            instructions_window,
            text=instructions_text,
            bg="#e6fff5",
            fg="#000000",
            font=("Arial", 12),
            justify="left",
        )
        instructions_label.pack()
    my_window = Tk()
    my_window.geometry("500x500+500+150")
    my_window.resizable(0, 0)
    my_window.title("Guest the Word Game")
    my_window.configure(background="#e6fff5")
    img1 = PhotoImage(file="back.png")

    lab_img1 = Button(
        my_window,
        image=img1,
        bg='#e6fff5',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)
    instructions_button = Button(
        my_window,
        text="Instructions",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        cursor="hand2",
        command=display_instructions,
    )
    instructions_button.pack(pady=(50, 20))

    my_window.mainloop()

main()

