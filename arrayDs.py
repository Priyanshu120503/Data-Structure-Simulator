import tkinter
import time
from tkinter import messagebox


class ArrayDs:
    def __init__(self, c, win):
        self.canvas = c
        self.window = win
        self.capacity = None
        self.created_arr = False
        self.box_dim = (50, 50)
        self.arr_data = {}

    def create_array(self, capacity):
        if self.created_arr:
            messagebox.showinfo(title='Invalid operation', message='Array already exists')
            return
        if capacity > 105:
            messagebox.showinfo(title='Screen Space insufficient', message='Cannot create array of size greater than 105')
            return
        if capacity <= 0:
            messagebox.showinfo(title='Invalid capacity', message=f'Cannot create array of size {capacity}')
            return
        self.capacity = capacity

        idx = 0
        self.created_arr = True
        for i in range(int(self.capacity/15) + 1):
            for j in range(15):
                rect_canvas = self.canvas.create_rectangle(50 + j*self.box_dim[0], 70 + 2*i*self.box_dim[1], 100 + j*self.box_dim[0], 120 + 2*i*self.box_dim[1])
                data_canvas = self.canvas.create_text(50 + int(self.box_dim[0]/2) + j*self.box_dim[0], 95 + 2*i*self.box_dim[1], font=('Courier', 18), text=0, anchor='c')
                idx_canvas = self.canvas.create_text(50 + int(self.box_dim[0]/2) + j*self.box_dim[0], 120 + 2*i*self.box_dim[1] + 10, text=idx, anchor='c')
                self.arr_data[idx] = [rect_canvas, idx_canvas, data_canvas]
                idx += 1
                if idx == self.capacity:
                    break
            if idx == self.capacity:
                break

    def insert(self, data, idx):
        if idx >= self.capacity or idx < 0:
            messagebox.showinfo(title='Invalid Index', message='No such index exists')
            return
        self.canvas.delete(self.arr_data[idx].pop())

        row, column = int(idx/15), idx % 15
        t = self.canvas.create_text(50 + int(self.box_dim[0] / 2) + column * self.box_dim[1], 0, text=data, font=('Courier', 18), anchor='c')
        final_y = 95 + 2*row*self.box_dim[1]
        self.move_along_y(t, final_y)
        self.arr_data[idx].append(t)

    def swap(self, idx1, idx2):
        if idx1 < 0 or idx1 >= self.capacity or idx2 < 0 or idx2 >= self.capacity:
            messagebox.showinfo(title='Invalid Index', message='Index out of range')
            return
        idx1_coords = self.canvas.coords(self.arr_data[idx1][-1])
        idx2_coords = self.canvas.coords(self.arr_data[idx2][-1])
        self.move_along_y(self.arr_data[idx1][-1], idx2_coords[1] + 50)
        self.move_along_x(self.arr_data[idx1][-1], idx2_coords[0])
        self.move_along_y(self.arr_data[idx1][-1], idx2_coords[1])
        self.move_along_y(self.arr_data[idx2][-1], idx1_coords[1] - 40)
        self.move_along_x(self.arr_data[idx2][-1], idx1_coords[0])
        self.move_along_y(self.arr_data[idx2][-1], idx1_coords[1])
        self.arr_data[idx1][-1], self.arr_data[idx2][-1] = self.arr_data[idx2][-1], self.arr_data[idx1][-1]

    def move_along_y(self, d, final_y):
        coords = self.canvas.coords(d)
        vel = 5 if final_y > coords[1] else -5
        while coords[1] != final_y:
            self.canvas.move(d, 0, vel)
            coords = self.canvas.coords(d)
            self.window.update()
            time.sleep(0.01)

    def move_along_x(self, d, final_x):
        coords = self.canvas.coords(d)
        vel = 5 if final_x > coords[0] else -5
        while coords[0] != final_x:
            self.canvas.move(d, vel, 0)
            coords = self.canvas.coords(d)
            self.window.update()
            time.sleep(0.01)


if __name__ == '__main__':
    window = tkinter.Tk()
    SCREEN_WIDTH = window.winfo_screenwidth()
    SCREEN_HEIGHT = window.winfo_screenheight()
    window.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
    canvas = tkinter.Canvas(window, width=int(0.6*SCREEN_WIDTH), height=SCREEN_HEIGHT, bg='#ffee38')

    a = ArrayDs(canvas, window)

    # -----------Frame-----------
    frame = tkinter.Frame(window, width=int(0.4*SCREEN_WIDTH), height=SCREEN_HEIGHT, bg='#b2e49c')
    capacity_var = tkinter.IntVar()
    cap_entry = tkinter.Entry(frame, textvariable=capacity_var, font=('Forte', 15), width=16)
    make_array_button = tkinter.Button(frame, text='Create Array', font=('Courier', 15, 'normal'), command=lambda: a.create_array(capacity_var.get()))
    of_size_label = tkinter.Label(frame, text='of size', font=('Courier', 15, 'normal'))

    data_var = tkinter.IntVar()
    idx_var = tkinter.IntVar()
    insert_button = tkinter.Button(frame, text='Insert', font=('Courier', 15, 'normal'), command=lambda: a.insert(data_var.get(), idx_var.get()))
    data_entry = tkinter.Entry(frame, textvariable=data_var, font=('Forte', 15), width=10)
    at_label = tkinter.Label(frame, text='at index', font=('Courier', 15, 'normal'))
    idx_entry = tkinter.Entry(frame, textvariable=idx_var, font=('Forte', 15), width=5)

    idx1_var = tkinter.IntVar()
    idx2_var = tkinter.IntVar()
    swap_button = tkinter.Button(frame, text='Swap', font=('Courier', 15, 'normal'), command=lambda: a.swap(idx1_var.get(), idx2_var.get()))
    idx1_entry = tkinter.Entry(frame, textvariable=idx1_var, font=('Forte', 15), width=5)
    idx2_entry = tkinter.Entry(frame, textvariable=idx2_var, font=('Forte', 15), width=5)

    make_array_button.place(x=80, y=550)
    of_size_label.place(x=250, y=550)
    cap_entry.place(x=350, y=550)
    insert_button.place(x=80, y=600)
    data_entry.place(x=180, y=600)
    at_label.place(x=300, y=600)
    idx_entry.place(x=420, y=600)
    swap_button.place(x=80, y=650)
    idx1_entry.place(x=150, y=650)
    idx2_entry.place(x=250, y=650)
    # ----------------------------

    canvas.place(x=0, y=0)
    frame.place(x=int(0.6*SCREEN_WIDTH), y=0)
    window.mainloop()
