import tkinter as tk
import calendar

text = calendar.calendar(2022)

root = tk.Tk()  # initializing the main window
# giving the main window the title and the geometry
root.geometry("500x600")
root.title("2022 Calendar")
label_1 = tk.Label(root, text="First Calendar in Python", bg='dark gray', font=('times', 28, 'italic'))
label_1.grid(row=1, column=1)

label_2 = tk.Label(root, text=text, font='consolas 10')
label_2.grid(row=2, column=1, padx=20)

if __name__ == '__main__':
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
