import tkinter
import math
import time
from tkinter import messagebox


def edge_coordinate(c1, c2, r):
    # Assuming c1 is above c2
    # Also assuming the origin is top left of screen and y increases as we go down
    if c1[0] == c2[0]:
        return c2[0], c2[1] - r, c2[0], c1[1] + r
    angle = math.degrees(math.atan((c2[1]-c1[1])/(c1[0]-c2[0])))
    if angle >= 0:
        print('Inside if')
        x1, y1 = c2[0] + r * math.cos(math.radians(angle)), c2[1] - r * math.sin(math.radians(angle))
        x2, y2 = c1[0] - r * math.cos(math.radians(angle)), c1[1] + r * math.sin(math.radians(angle))
    else:
        angle = -angle
        x1, y1 = c2[0] - r * math.cos(math.radians(angle)), c2[1] - r * math.sin(math.radians(angle))
        x2, y2 = c1[0] + r * math.cos(math.radians(angle)), c1[1] + r * math.sin(math.radians(angle))
    return round(x1), round(y1), round(x2), round(y2)


class Node:
    def __init__(self, can, win, data, x, y, radius, parent):
        self.canvas = can
        self.window = win
        self.data = data
        self.x = x
        self.y = y
        self.radius = radius
        self.children = []
        self.parent = parent
        self.node = self.canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill='white', width=3)
        self.coordinates = [self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius]
        self.text = self.canvas.create_text(self.x, self.y, text=self.data, anchor='c')
        self.edges = []

    # def create_edge(self):
    #     coords = edge_coordinate((self.parent.x, self.parent.y), (self.x, self.y), self.radius)
    #     self.edges.append(self.canvas.create_line(coords))

    # def add_child(self, data, x, y):
    #     self.children.append(Node(self.canvas, self.window, data, x, y, self.radius, self))
    #     coords = edge_coordinate((self.x, self.y), (x, y), self.radius)
    #     self.edges.append(self.canvas.create_line(coords))
    #     return self

    def add_child(self, data, x, y):
        n = Node(self.canvas, self.window, data, self.x, self.y, self.radius, self)
        x_dist, y_dist = (x - self.x), (y - self.y)
        x_vel, y_vel = round(x_dist/10), round(y_dist/10)
        print(x_vel, y_vel)
        coord = self.canvas.coords(n.node)
        while coord[0] + self.radius < x or coord[1] + self.radius < y:
            self.canvas.move(n.node, x_vel, y_vel)
            self.canvas.move(n.text, x_vel, y_vel)
            coord = self.canvas.coords(n.node)
            self.window.update()
            time.sleep(0.01)
        n.x, n.y = x, y
        self.children.append(n)
        coords = edge_coordinate((self.x, self.y), (x, y), self.radius)
        self.edges.append(self.canvas.create_line(coords))
        return self

    def remove_edge(self, child_idx):
        self.canvas.delete(self.edges[child_idx])
        self.edges.pop(child_idx)


class Tree:
    def __init__(self, c, win):
        self.canvas = c
        self.window = win
        self.size = 0
        self.root = None
        self.y_coordinates = [100, 250, 400, 550, 700]
        self.current = None
        self.current_depth = 0
        self.childs_in_depth = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        self.temp_circle = None
        self.i = 0
        self.child_index = 0
        self.size = 0
        self.first_time = True
        self.size_text = self.canvas.create_text(700, 100, anchor='nw', text='Size = ', font=('Courier', 15, 'normal'))
        self.size_and_capacity_text = []
        self.write_size_and_capacity()

    def write_size_and_capacity(self):
        if not self.first_time:
            self.canvas.delete(self.size_and_capacity_text[-1])
        t = self.canvas.create_text(780, 100, anchor='nw', text=self.size, font=('Courier', 15, 'normal'))
        self.size_and_capacity_text.append(t)
        self.first_time = False

    def add_root(self, data):
        if self.root:
            messagebox.showinfo(title='Invalid Operation', message='Root already exists')
            return
        self.root = Node(self.canvas, self.window, data, 100, self.y_coordinates[0], 40, None)
        self.current = self.root
        self.size += 1
        self.highlight_current([60, 60, 140, 140])
        self.write_size_and_capacity()

    def highlight_current(self, c):
        print(c)
        self.temp_circle = self.canvas.create_oval(c[0], c[1], c[2], c[3], outline='blue', width=4)

    def remove_highlight(self):
        self.canvas.delete(self.temp_circle)

    def add_child(self, data):
        # Node(self.canvas, self.window, data, 120, self.y_coordinates[1], 40, self.root)
        if not self.root:
            messagebox.showinfo(title='Invalid Operation', message='Add root first')
            return
        # self.current.children.append(self.current.add_child(data, 120 + self.i*100, self.y_coordinates[self.current_depth+1]))
        self.current.add_child(data, 100 + 150*self.childs_in_depth[self.current_depth+1], self.y_coordinates[self.current_depth+1])
        self.childs_in_depth[self.current_depth+1] += 1
        print(self.current.children)
        self.size += 1
        self.write_size_and_capacity()

    def goto_parent(self):
        if self.current == self.root:
            messagebox.showinfo(title='Invalid choice', message='No Parent for Root node')
            return
        elif not self.root:
            messagebox.showinfo(title='Invalid choice', message='Create a tree first!')
            return
        self.remove_highlight()
        self.current = self.current.parent
        self.current_depth -= 1
        self.highlight_current(self.canvas.coords(self.current.node))

    def goto_children(self):
        if len(self.current.children) == 0:
            messagebox.showinfo(title='Invalid choice', message='No Children')
            return
        self.remove_highlight()
        self.child_index = 0
        print(self.current.children)
        self.current = self.current.children[0]
        print(f'Inside goto child {self.current}')
        print(f'Inside goto child {self.canvas.coords(self.current.node)}')
        self.current_depth += 1
        self.highlight_current(self.canvas.coords(self.current.node))

    def goto_next_child(self):
        self.child_index = self.current.parent.children.index(self.current)
        if self.child_index == len(self.current.parent.children) - 1:
            messagebox.showinfo(title='Invalid choice', message='No Next child')
            return
        self.remove_highlight()
        print(self.current)
        self.current = self.current.parent
        print(self.current)
        self.child_index += 1
        self.current = self.current.children[self.child_index]
        self.highlight_current(self.canvas.coords(self.current.node))

    def goto_prev_child(self):
        self.child_index = self.current.parent.children.index(self.current)
        if self.child_index == 0:
            messagebox.showinfo(title='Invalid choice', message='No Previous child')
            return
        self.remove_highlight()
        print(self.current)
        self.current = self.current.parent
        print(self.current)
        self.child_index -= 1
        self.current = self.current.children[self.child_index]
        self.highlight_current(self.canvas.coords(self.current.node))


if __name__ == '__main__':
    window = tkinter.Tk()
    SCREEN_WIDTH = window.winfo_screenwidth()
    SCREEN_HEIGHT = window.winfo_screenheight()
    window.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
    canvas = tkinter.Canvas(window, width=int(0.6 * SCREEN_WIDTH), height=SCREEN_HEIGHT, bg='#ffee38')

    t = Tree(canvas, window)

    # -----------Frame-----------
    frame = tkinter.Frame(window, width=int(0.4 * SCREEN_WIDTH), height=SCREEN_HEIGHT, bg='#b2e49c')
    entry_var = tkinter.StringVar()
    root_var = tkinter.StringVar()

    root_entry = tkinter.Entry(frame, textvariable=root_var, font=('Forte', 15), width=16)
    add_root_button = tkinter.Button(frame, text='Add Root', font=('Forte', 15), width=16, command=lambda: t.add_root(root_var.get()))

    value_entry = tkinter.Entry(frame, textvariable=entry_var, font=('Forte', 15), width=16)
    insert_button = tkinter.Button(frame, text='Add child', font=('Courier', 15, 'normal'), command=lambda: t.add_child(entry_var.get()))
    goto_child_button = tkinter.Button(frame, text='Goto Child', font=('Courier', 15, 'normal'), command=t.goto_children)
    next_child_button = tkinter.Button(frame, text='Next Child', font=('Courier', 15, 'normal'), command=t.goto_next_child)
    prev_child_button = tkinter.Button(frame, text='Previous Child', font=('Courier', 15, 'normal'), command=t.goto_prev_child)
    goto_parent_button = tkinter.Button(frame, text='Goto Parent', font=('Courier', 15, 'normal'), command=t.goto_parent)

    root_entry.place(x=80, y=500)
    add_root_button.place(x=290, y=500)
    value_entry.place(x=80, y=550)
    insert_button.place(x=290, y=550)
    goto_child_button.place(x=80, y=600)
    next_child_button.place(x=240, y=600)
    prev_child_button.place(x=410, y=600)
    goto_parent_button.place(x=80, y=650)
    # ----------------------------

    canvas.place(x=0, y=0)
    frame.place(x=int(0.6 * SCREEN_WIDTH), y=0)
    window.mainloop()
