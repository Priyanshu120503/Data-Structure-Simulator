# Queue

import tkinter
import time
from tkinter import messagebox


class Queue:
    def __init__(self, c, win):
        self.canvas = c
        self.window = win
        self.space_btw_boxes = 150
        self.path_left1_line = self.canvas.create_line(50, 70, 50, 750, fill='black', width=4)
        self.path_right1_line = self.canvas.create_line(200, 70, 200, 580, fill='black', width=4)
        self.path_bottom1_line = self.canvas.create_line(50, 750, 800, 750, fill='black', width=4)
        self.path_bottom2_line = self.canvas.create_line(200, 580, 650, 580, fill='black', width=4)
        self.path_left2_line = self.canvas.create_line(800, 750, 800, 70, fill='black', width=4)
        self.path_right2_line = self.canvas.create_line(650, 580, 650, 70, fill='black', width=4)
        self.size = 0
        self.path_coordinates = [(660, 0), (660, 600), (60, 600), (60, 150)]
        self.box_create_coordinates = (660, 10, 790, 140)
        self.text_create_coordinates = (725, 75)
        self.boxes = []
        self.text = []
        self.first_time = True
        self.size_and_capacity_text = []
        self.size_text = self.canvas.create_text(350, 450, anchor='nw', text='Size = ', font=('Courier', 15, 'normal'))
        self.capacity_text = self.canvas.create_text(350, 480, anchor='nw', text='Capacity = 11', font=('Courier', 15, 'normal'))
        self.write_size_and_capacity()

    def enqueue(self, data):
        if self.size == 11:
            messagebox.showinfo(title='Queue Full', message='Cannot add more elements')
            return

        create_box = self.canvas.create_rectangle(self.box_create_coordinates, outline='black', fill='light blue', width =2)
        text = self.canvas.create_text(self.text_create_coordinates, anchor='c', text=data, font=('Arial', 24), fill='black')
        if self.size < 4:
            final_box_y = 150+self.space_btw_boxes*self.size

            self.move_along_right(create_box, text, 600)
            self.move_along_bottom(create_box, text, 60)
            self.move_along_left(create_box, text, final_box_y)

        elif 4 <= self.size <= 7:
            final_box_x = 210 + self.space_btw_boxes*(self.size-4)

            self.move_along_right(create_box, text, 600)
            self.move_along_bottom(create_box, text, final_box_x)

        elif self.size >= 8:
            final_box_y = 600 - self.space_btw_boxes * (self.size-7)

            self.move_along_right(create_box, text, final_box_y)

        self.text.append(text)
        self.boxes.append(create_box)
        self.size += 1
        print(self.size)
        self.write_size_and_capacity()

    def dequeue(self):
        if self.size == 0:
            messagebox.showinfo(title='Queue Empty', message='No elements to dequeue')
            return
        self.move_along_left(self.boxes[0], self.text[0], 0)
        self.canvas.delete(self.boxes[0])
        self.canvas.delete(self.text[0])
        self.boxes.pop(0)
        self.text.pop(0)
        self.size -= 1
        i, j, k = 0, 0, 0
        for box, text, i in zip(self.boxes, self.text, range(min(self.size, 3))):
            self.move_along_left(box, text, 150 + self.space_btw_boxes * i)
        for box, text, j in zip(self.boxes[i+1:], self.text[i+1:], range(min(self.size-3, 4))):
            self.move_along_bottom(box, text, 60 + self.space_btw_boxes*j)
        for box, text, k in zip(self.boxes[3+j+1:], self.text[3+j+1:], range(min(self.size-7, 3))):
            self.move_along_right(box, text, 600 - self.space_btw_boxes * k)
        self.write_size_and_capacity()

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.size == 0:
            messagebox.showinfo(title='Queue Empty', message='There are no elements in the queue')
            return

        coordinates = self.canvas.coords(self.boxes[0])

        top_line = self.canvas.create_line(coordinates[0], coordinates[1], coordinates[2],
                                           coordinates[1], fill='white', width=6)
        left_line = self.canvas.create_line(coordinates[0], coordinates[1], coordinates[0],
                                            coordinates[3], fill='white', width=6)
        right_line = self.canvas.create_line(coordinates[2], coordinates[1], coordinates[2],
                                             coordinates[3], fill='white', width=6)
        bottom_line = self.canvas.create_line(coordinates[0], coordinates[3], coordinates[2],
                                              coordinates[3], fill='white', width=6)
        self.window.update()
        time.sleep(1)
        self.canvas.delete(top_line, left_line, right_line, bottom_line)

    def write_size_and_capacity(self):
        if not self.first_time:
            self.canvas.delete(self.size_and_capacity_text[-1])
        t = self.canvas.create_text(450, 450, anchor='nw', text=self.size, font=('Courier', 15, 'normal'))
        self.size_and_capacity_text.append(t)
        self.first_time = False

    def move_along_right(self, obj1, obj2, final_y):
        coordinates = self.canvas.coords(obj1)
        while coordinates[1] != final_y:
            self.canvas.move(obj1, 0, 5)
            self.canvas.move(obj2, 0, 5)
            coordinates = self.canvas.coords(obj1)
            self.window.update()
            time.sleep(0.01)

    def move_along_bottom(self, obj1, obj2, final_x):
        coordinates = self.canvas.coords(obj1)
        while coordinates[0] != final_x:
            self.canvas.move(obj1, -5, 0)
            self.canvas.move(obj2, -5, 0)
            coordinates = self.canvas.coords(obj1)
            self.window.update()
            time.sleep(0.01)

    def move_along_left(self, obj1, obj2, final_y):
        coordinates = self.canvas.coords(obj1)
        while coordinates[1] >= final_y:
            self.canvas.move(obj1, 0, -5)
            self.canvas.move(obj2, 0, -5)
            coordinates = self.canvas.coords(obj1)
            self.window.update()
            time.sleep(0.01)


if __name__ == '__main__':

    window = tkinter.Tk()
    SCREEN_WIDTH = window.winfo_screenwidth()
    SCREEN_HEIGHT = window.winfo_screenheight()
    window.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
    canvas = tkinter.Canvas(window, width=int(0.6*SCREEN_WIDTH), height=SCREEN_HEIGHT, bg='#ffee38')
    frame = tkinter.Frame(window, width=int(0.4*SCREEN_WIDTH), height=SCREEN_HEIGHT, bg='#b2e49c')
    q = Queue(canvas, window)

    entry_var = tkinter.StringVar()
    enqueue_entry = tkinter.Entry(frame, textvariable=entry_var, font=('Forte', 15), width=16)
    enqueue_button = tkinter.Button(frame, text='Enqueue', font=('Courier', 15), width=16, command=lambda: q.enqueue(entry_var.get()))
    dequeue_button = tkinter.Button(frame, text='Dequeue', font=('Courier', 15), width=16, command=q.dequeue)

    enqueue_button.place(x=290, y=550)
    enqueue_entry.place(x=80, y=550)
    dequeue_button.place(x=80, y=600)
    canvas.place(x=0, y=0)
    frame.place(x=int(0.6*SCREEN_WIDTH), y=0)

    window.mainloop()



