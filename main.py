from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    win.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_title, text='French', fill='black')
    canvas.itemconfig(canvas_word, text=f"{current_card['French']}", fill='black')
    canvas.itemconfig(card_background, image=front_image)

    flip_timer = win.after(3000, flip_card)


def flip_card():

    canvas.itemconfig(canvas_title, text='English', fill='white')
    canvas.itemconfig(canvas_word, text=f"{current_card['English']}", fill='white')
    canvas.itemconfig(card_background, image=back_image)


def is_known():
    global to_learn
    to_learn.remove(current_card)

    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv(r'data/word_to_learn.csv', index=False)
    next_card()



win = Tk()
win.title("Flashy")
win.config(pady=50, padx=50, background=BACKGROUND_COLOR)
back_image = PhotoImage(file=r"images/card_back.png")
front_image = PhotoImage(file=r"images/card_front.png")
right_image = PhotoImage(file=r"images/right.png")
wrong_image = PhotoImage(file=r"images/wrong.png")


flip_timer = win.after(3000, flip_card)

canvas = Canvas(width=800, height=536, highlightthickness=0, background=BACKGROUND_COLOR)
card_background = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)

canvas_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=('Ariel', 48, 'bold'))


cross_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

check_button = Button(image=right_image, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

next_card()





win.mainloop()
