import time
import tkinter
from tkinter import *
import customtkinter
import random
# workflow: click start - typing - 60s - auto calculate the right word - calculate the speed - display in the scoreboard

possibleTexts = [
    'For writers, a random sentence can help them get their creative juices flowing. Since the topic of the sentence is completely unknown, it forces the writer to be creative when the sentence appears. There are a number of different ways a writer can use the random sentence for creativity. The most common way to use the sentence is to begin a story. Another option is to include it somewhere in the story. A much more difficult challenge is to use it to end a story. In any of these cases, it forces the writer to think creatively since they have no idea what sentence will appear from the tool.',
    'The goal of Python Code is to provide Python tutorials, recipes, problem fixes and articles to beginner and intermediate Python programmers, as well as sharing knowledge to the world. Python Code aims for making everyone in the world be able to learn how to code for free. Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.',
    'As always, we start with the imports. Because we make the UI with tkinter, we need to import it. We also import the font module from tkinter to change the fonts on our elements later. We continue by getting the partial function from functools, it is a genius function that excepts another function as a first argument and some args and kwargs and it will return a reference to this function with those arguments. This is especially useful when we want to insert one of our functions to a command argument of a button or a key binding.'
]

text = random.choice(possibleTexts).lower()




# screen
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.minsize(500,400)
app.title('Test Your Speed')


def count_time():
    for t in range(60):
        app.after(1000)
        count_text()

def count_text():
    for i in range(len(typed_text.get('1.0', 'end-1c').split())):
        n = 0
        if all_text_list[i] == typed_text_list[i]:
            n += 1
        score = customtkinter.CTkLabel(master=app, text=f"Your Test Score: {n} per minute")
        score.place(relx=0.7, rely=0.1, anchor=tkinter.CENTER)



# start Button
count_down_button = customtkinter.CTkButton(master=app, text="Start", command=count_time)
count_down_button.place(relx=0.3, rely=0.2,anchor=tkinter.CENTER)

# restart Button
button = customtkinter.CTkButton(master=app, text="Restart", command=count_time)
button.place(relx=0.7, rely=0.2,anchor=tkinter.CENTER)

#TODO scoreboard
# Label for score
label = customtkinter.CTkLabel(master=app, text="Start to test your typing speed!")
label.place(relx=0.3, rely=0.1,anchor=tkinter.CENTER)


#TODO text
# Label for text
all_text = Text(app, width=60,height=10)
all_text.place(relx=0.5, rely=0.4,anchor=tkinter.CENTER)
all_text.insert(tkinter.END,text)
# Entry for text
typed_text= Text(app, width=60,height=10)
typed_text.place(relx=0.5, rely=0.7,anchor=tkinter.CENTER)

all_text_list = all_text.get('1.0','end-1c').split()
typed_text_list = typed_text.get('1.0','end-1c').split()



app.mainloop()