# Stack

import tkinter
import time
from tkinter import messagebox


class Stack:
    def __init__(self, c, win):
        self.canvas = c
        self.window = win
        self.capacity = 8
        self.BOX_HEIGHT = 50
        self.container_left_line = self.canvas.create_line(270, 300, 270, 300 + self.capacity*self.BOX_HEIGHT, fill='white', width=3)
        self.container_right_line = self.canvas.create_line(570, 300, 570, 300 + self.capacity*self.BOX_HEIGHT, fill='white', width=3)
        self.container_bottom_line = self.canvas.create_line(270, 300 + self.capacity*self.BOX_HEIGHT, 570, 300 + self.capacity*self.BOX_HEIGHT, fill='white', width=3)
        self.size = 0
        self.lines = [self.container_bottom_line]
        self.text = []
        self.size_text = self.canvas.create_text(700, 700, anchor='nw', text='Size = ', font=('Courier', 15, 'normal'))
        self.capacity_text = self.canvas.create_text(700, 730, anchor='nw', text='Capacity = 13', font=('Courier', 15, 'normal'))
        self.size_and_capacity_text = []
        self.first_time = True
        self.write_size_and_capacity()

    def write_size_and_capacity(self):
        if not self.first_time:
            self.canvas.delete(self.size_and_capacity_text[-1])
        t = self.canvas.create_text(780, 700, anchor='nw', text=self.size, font=('Courier', 15, 'normal'))
        self.size_and_capacity_text.append(t)
        self.first_time = False

    def push(self, data):
        if self.size == 13:
            messagebox.showinfo(title='Stack Full', message='Cannot add more elements')
            return
        coordinates = self.canvas.coords(self.lines[-1])
        # text = self.canvas.create_text(420, 0, anchor='c', text=data, font=('Arial', 30), fill='white')
        # self.text.append(text)

        text, val = self.canvas.create_text(420, 0, anchor='c', text=data, font=('Arial', 30), fill='white'), data
        self.text.append((text, val))

        final_y = coordinates[1]-25
        text_coords = self.canvas.coords(text)

        # Entry animation
        while text_coords[1] != final_y:
            self.canvas.move(text, 0, 5)
            self.window.update()
            text_coords = self.canvas.coords(text)
            time.sleep(0.01)

        new_line = self.canvas.create_line(270, coordinates[1]-self.BOX_HEIGHT, 570, coordinates[1]-self.BOX_HEIGHT, fill='white', width=3)
        self.lines.append(new_line)
        self.size += 1
        if self.size >= 7 and self.capacity < 13:
            self.capacity += 1
            temp_left = self.container_left_line
            temp_y_cor = self.canvas.coords(temp_left)[1]
            self.canvas.delete(self.container_left_line)
            self.canvas.delete(self.container_right_line)
            self.container_left_line = self.canvas.create_line(270, temp_y_cor-self.BOX_HEIGHT, 270, 300 + 8*self.BOX_HEIGHT, fill='white', width=3)
            self.container_right_line = self.canvas.create_line(570, temp_y_cor-self.BOX_HEIGHT, 570, 300 + 8*self.BOX_HEIGHT, fill='white', width=3)
        print(f'Size = {self.size}     Capa = {self.capacity}')
        self.write_size_and_capacity()

    def pop(self):
        if self.size == 0:
            messagebox.showinfo(title='Stack Empty', message='No elements to pop')
            return
        self.canvas.delete(self.lines[-1])

        # Exit animation
        final_y = 0
        text_coords = self.canvas.coords(self.text[-1][0])
        popped_value = self.text[-1][1]
        # text_coords = self.canvas.coords(self.text[-1])
        while text_coords[1] != final_y:
            self.canvas.move(self.text[-1][0], 0, -5)
            # self.canvas.move(self.text[-1], 0, -5)
            self.window.update()
            text_coords = self.canvas.coords(self.text[-1][0])
            # text_coords = self.canvas.coords(self.text[-1])
            time.sleep(0.01)

        self.canvas.delete(self.text[-1][0])
        # self.canvas.delete(self.text[-1])
        self.lines.pop()
        self.text.pop()
        self.size -= 1
        if 6 <= self.size < 11:
            temp_left = self.container_left_line
            temp_y_cor = self.canvas.coords(temp_left)[1]
            self.canvas.delete(self.container_left_line)
            self.canvas.delete(self.container_right_line)
            self.container_left_line = self.canvas.create_line(270, temp_y_cor+self.BOX_HEIGHT, 270, 300 + 8*self.BOX_HEIGHT, fill='white', width=3)
            self.container_right_line = self.canvas.create_line(570, temp_y_cor+self.BOX_HEIGHT, 570, 300 + 8*self.BOX_HEIGHT, fill='white', width=3)
        if self.size < 11 and self.capacity > 8:
            self.capacity -= 1
        print(f'Size = {self.size}     Capa = {self.capacity}')
        self.write_size_and_capacity()
        return popped_value

    def peek(self):
        if self.size == 0:
            messagebox.showinfo(title='Stack Empty', message='There are no elements in the stack')
            return

        top_line_coordinates = self.canvas.coords(self.lines[-1])
        bottom_line_coordinates = self.canvas.coords(self.lines[-2])
        print(top_line_coordinates, bottom_line_coordinates)

        top_line = self.canvas.create_line(top_line_coordinates[0], top_line_coordinates[1], top_line_coordinates[2], top_line_coordinates[3], fill='blue', width=6)
        left_line = self.canvas.create_line(top_line_coordinates[0], top_line_coordinates[1], top_line_coordinates[0], bottom_line_coordinates[1], fill='blue', width=6)
        right_line = self.canvas.create_line(top_line_coordinates[2], top_line_coordinates[1], top_line_coordinates[2], bottom_line_coordinates[1], fill='blue', width=6)
        bottom_line = self.canvas.create_line(bottom_line_coordinates[0], bottom_line_coordinates[1], bottom_line_coordinates[2], bottom_line_coordinates[3], fill='blue', width=6)
        self.window.update()
        time.sleep(1)
        self.canvas.delete(top_line, left_line, right_line, bottom_line)

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def pow(self, a, b):
        return a ** b

    def evaluate(self, exp):
        print(exp)
        operations = {'+': self.add, '-': self.sub, '*': self.mul, '/': self.div, '^': self.pow}
        for i in exp.split():
            print(i)
            if i.isnumeric():
                self.push(i)
            elif i in ('+', '-', '*', '/', '^'):
                num1 = float(self.pop())
                num2 = float(self.pop())
                ans = operations[i](num2, num1)
                self.push(round(ans, 6))

    def is_empty(self):
        return self.size == 0


if __name__ == '__main__':
    window = tkinter.Tk()
    SCREEN_WIDTH = window.winfo_screenwidth()
    SCREEN_HEIGHT = window.winfo_screenheight()
    window.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
    canvas = tkinter.Canvas(window, width=int(0.6*SCREEN_WIDTH), height=SCREEN_HEIGHT, bg='#ffee38')

    s = Stack(canvas, window)

    # -----------Frame-----------
    frame = tkinter.Frame(window, width=int(0.4*SCREEN_WIDTH), height=SCREEN_HEIGHT, bg='#b2e49c')
    entry_var = tkinter.StringVar()
    push_entry = tkinter.Entry(frame, textvariable=entry_var, font=('Forte', 15), width=16)
    push_button = tkinter.Button(frame, text='Push', font=('Courier', 15, 'normal'), command=lambda: s.push(entry_var.get()))
    pop_button = tkinter.Button(frame, text='Pop', font=('Courier', 15, 'normal'), command=s.pop)
    peek_button = tkinter.Button(frame, text='Peek', font=('Courier', 15, 'normal'), command=s.peek)

    expression = tkinter.StringVar()
    postfix_entry = tkinter.Entry(frame, textvariable=expression, font=('Courier', 15, 'normal'), width=20)
    done_button = tkinter.Button(frame, text="Evaluate", font=('Courier', 15, 'normal'), command=lambda: s.evaluate(expression.get()))

    postfix_entry.place(x=80, y=400)
    done_button.place(x=300, y=400)
    push_entry.place(x=80, y=550)
    push_button.place(x=290, y=550)
    pop_button.place(x=80, y=600)
    peek_button.place(x=50, y=650)
    # ----------------------------

    canvas.place(x=0, y=0)
    frame.place(x=int(0.6*SCREEN_WIDTH), y=0)
    window.mainloop()
