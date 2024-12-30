from tkinter import *
from tkinter import ttk




#label = Label(root, width =30, height = 2, text = '', font = ('arial',30)) # создаем текстовую метку
#label.configure(bg='#2a2d36')
#label.pack() # размещаем метку в окне

clicks = 0

def click_button():
    global clicks
    clicks += 1
    btn['text'] = f'Clicks {clicks}'

root = Tk()
root.title('First window')
root.geometry('200x200')

btn = ttk.Button(text = 'Click Me', command=click_button) # создание кнопки
btn.pack()


root.mainloop()



