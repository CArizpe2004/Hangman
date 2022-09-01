import os
from tkinter import *
from PIL import ImageTk, Image

found = ''
guesses = 0
indexes = {}
photo_list = {}

# path = r'C:\Users\Cesar\PythonProjects\.vscode\Hangman\Hangman Photos'

# for i in os.listdir(path):

#     full_path = os.path.join(path, i)
#     photo_list[i] = full_path

# for i in photo_list:
#     print(i + ' --- ' + photo_list[i])

def check_in_word(word, label, button, entry, guess_text, prompt):
    global found
    global guesses
    guess = entry.get()
    guess = guess.strip()
    guess = guess.upper()
    entry.delete(0, 'end')
    print(guess)
    print(word)

    try:
        word.index(guess)
        if guess == word:
            for i in range(len(word)):
                indexes[i] = guess[i]
        else:
            for i in range(len(word)):
                if word[i] == guess:
                    indexes[i] = guess
        prompt['text'] = ' '
    except:
        guesses += 1
        prompt['text'] = 'Incorrect guess'
        
    found = ''
    for i in range(len(word)):
        if i in indexes:
            found += indexes[i] + ' '
        else:
            found += '- '
    guess_text['text'] = found

    check = ''
    for i in range(len(found)):
        if found[i] != ' ':
            check += found[i]
    if check == word or guess == word:
        label['text'] = 'You Win!'
        print('winner')
        button.destroy()
        entry.destroy()
    if guesses == 5:
        label['text'] = 'You Lose.'
        button.destroy()
        entry.destroy()
    print(guesses)

def get_char(word, label, button, entry, guess_label):
    label['text'] = 'Enter a letter'

    guess_prompt = Label(root, text='', fg='red', bg='#0d0c0a')
    guess_prompt.place(relx=.5, rely=.52, anchor=N)

    button.config(command= lambda: check_in_word(word, label, button, entry, guess_label, guess_prompt))
    
def get_char_and_destroy(label, button, entry):
    word = entry.get()
    entry.delete(0, 'end')
    word = word.strip()
    word = word.upper()

    guess_label = Label(root, text='_ ' * len(word), fg='white', background='#0d0c0a')
    guess_label.config(font=('Helvatical bold', 60))
    guess_label.place(relx=.5, rely=1, anchor=S)
    
    get_char(word, label, button, entry, guess_label)

def get_word():
    enter_label = Label(root, text='Enter a Word', fg='white', bg='#0d0c0a')
    enter_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    # img = ImageTk.PhotoImage(Image.open(photo_list['Stand.png']))
    
    submission_box = Entry(root, bg='#0d0c0a', fg='white', insertbackground='white')
    submission_box.config(highlightcolor='white')

    submission_box.place(x=390, y=450)
    word_label = Label(root, text=found, fg='white', background='#0d0c0a')

    word_label.config(font=('Helvatical bold', 60))
    enter_button = Button(root, text='Enter', bg='grey', command= lambda: get_char_and_destroy(enter_label, enter_button, submission_box))    
    enter_button.place(x=390, y=470)

def get_word_and_hide(button):
    button.destroy()
    get_word()

root = Tk()
root.geometry('900x800')
root.config(bg='#0d0c0a')
root.title('Hangman')

play_button = Button(root, text='Play', bg='grey', height=5, width=10, command= lambda: get_word_and_hide(play_button))
play_button.place(relx=.5, rely=.5, anchor=CENTER)

mainloop()