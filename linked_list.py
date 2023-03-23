import tkinter
from tkinter import messagebox


class Node:
    def __init__(self, c, x, y, width, height, arrow_box_width, data, arrow_direction, has_next=None):
        self.canvas = c
        self.data_rect = self.canvas.create_rectangle(x, y, x+width, y+height, fill='white', outline='black', width=2)
        self.arrow_rect = self.canvas.create_rectangle(x+width, y, x+width+arrow_box_width, y+height, fill='white', outline='black', width=2)
        self.right_arrow_photo = tkinter.PhotoImage(file='images/right-arrow_2.png')
        self.left_arrow_photo = tkinter.PhotoImage(file='images/left_arrow.png')
        self.down_arrow_photo = tkinter.PhotoImage(file='images/down_arrow.png')
        self.arrow = None
        self.has_next = has_next
        self.arrow_direction = arrow_direction
        self.data = data
        self.data_rect_coords = self.canvas.coords(self.data_rect)
        self.text = self.canvas.create_text(x + int(width/2), y + int(height/2), text=data, font=('Arial', 10), fill='green', anchor='c')
        if self.has_next:
            self.create_arrow()

    def create_arrow(self):
        arrow_rect_coordinates = self.canvas.coords(self.arrow_rect)
        coords = (int((arrow_rect_coordinates[0] + arrow_rect_coordinates[2]) / 2),
                  int((arrow_rect_coordinates[1] + arrow_rect_coordinates[3]) / 2))
        temp_photo = None
        if self.arrow_direction == 'r':
            self.arrow = self.canvas.create_image(coords, image=self.right_arrow_photo, anchor='w')
            temp_photo = self.right_arrow_photo
        elif self.arrow_direction == 'l':
            self.arrow = self.canvas.create_image(coords, image=self.left_arrow_photo, anchor='e')
            temp_photo = self.left_arrow_photo
        elif self.arrow_direction == 'd':
            self.arrow = self.canvas.create_image(coords, image=self.down_arrow_photo, anchor='n')
            temp_photo = self.down_arrow_photo

        # To prevent the image from being collected by garbage collector
        temp = tkinter.Label(None, image=temp_photo)
        temp.image = temp_photo

    def remove_arrow(self):
        self.canvas.delete(self.arrow)

    def delete_node(self):
        self.canvas.delete(self.text)
        self.remove_arrow()
        self.canvas.delete(self.data_rect, self.arrow_rect, self.arrow)
        del self

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self, canvas, window):
        self.canvas = canvas
        self.window = window
        self.size = 0
        self.index = -1
        self.DATA_BOX_WIDTH = 100
        self.BOX_HEIGHT = 40
        self.ARROW_BOX_WIDTH = 40
        self.data = []
        self.coordinates = {}
        for (i, line_no) in zip(range(50, 651, 200), range(1, 8, 2)):
            for j, element_no in zip(range(50, 651, 200), range(4)):
                arrow_dir = 'r'
                if j == 650:
                    arrow_dir = 'd'
                self.coordinates[(line_no - 1) * 4 + element_no] = (j, i, self.DATA_BOX_WIDTH, self.BOX_HEIGHT, self.ARROW_BOX_WIDTH, arrow_dir)
        for (i, line_no) in zip(range(150, 651, 200), range(2, 8, 2)):
            for j, element_no in zip(range(790, 189, -200), range(4)):
                arrow_dir = 'l'
                if j == 190:
                    arrow_dir = 'd'
                self.coordinates[(line_no - 1) * 4 + element_no] = (
                j, i, -self.DATA_BOX_WIDTH, self.BOX_HEIGHT, -self.ARROW_BOX_WIDTH, arrow_dir)

        self.nodes = []
        self.index_canvas = []

    def insert(self, data, idx):
        if (self.size == 0 and idx != 0) or (idx > self.size != 0) or idx < 0:
            messagebox.showinfo(title='Invalid Index', message=f'Index {idx} is out of range')
            return

        if idx == self.size:
            d = self.coordinates[idx]
            self.nodes.append(Node(self.canvas, d[0], d[1], d[2], d[3], d[4], data, d[5], False))
            self.index_canvas.append(self.canvas.create_text(d[0] + d[2] / 100 * 70, d[1] + 55, text=idx, font=('Arial', 18), fill='white',
                                    anchor='c'))
            if idx > 0:
                self.nodes[-2].has_next = True
                self.nodes[-2].create_arrow()
        elif 0 <= idx < self.size:
            self.nodes.append('')
            for i in range(self.size, idx, -1):
                d = self.coordinates[i]
                if i == self.size:
                    self.nodes[i] = Node(self.canvas, d[0], d[1], d[2], d[3], d[4], self.nodes[-2].__str__(), d[5], False)
                    self.index_canvas.append(
                        self.canvas.create_text(d[0] + d[2] / 100 * 70, d[1] + 55, text=i, font=('Arial', 18),
                                                fill='white',
                                                anchor='c'))
                else:
                    self.nodes[i].delete_node()
                    self.nodes[i] = Node(self.canvas, d[0], d[1], d[2], d[3], d[4], self.nodes[i-1].__str__(), d[5], True)

            d = self.coordinates[idx]
            self.nodes[idx] = Node(self.canvas, d[0], d[1], d[2], d[3], d[4], data, d[5], True)
        self.data.append(data)
        self.size += 1
        print(self.nodes)

    def remove(self, idx):
        if self.size == 0 or (idx >= self.size != 0) or idx < 0:
            messagebox.showinfo(title='Invalid Index', message=f'Index {idx} is out of range')
            return

        print(self.nodes, self.size)
        if idx == 1 and self.size == 2:
            self.canvas.delete('all')
            print('Inside if')
            temp_data = self.nodes[0]
            d = self.coordinates[0]
            self.index_canvas = [self.canvas.create_text(d[0] + d[2] / 100 * 70, d[1] + 55, text=0, font=('Arial', 18), fill='white',
                                    anchor='c')]
            self.nodes = [Node(self.canvas, d[0], d[1], d[2], d[3], d[4], temp_data, d[5], False)]
            self.size -= 1
        elif idx == self.size-1:
            print('Inside elif')
            self.nodes[-1].delete_node()
            self.canvas.delete(self.index_canvas[-1])
            self.index_canvas.pop()
            self.nodes.pop()
            self.size -= 1
            if self.size != 0:
                self.nodes[-1].has_next = False
                self.nodes[-1].remove_arrow()
        else:
            print('Inside 2nd elif')

            for i in range(idx, self.size-1, 1):
                d = self.coordinates[i]
                self.nodes[i].remove_arrow()
                self.nodes[i].delete_node()
                temp_data = self.nodes[i+1].__str__()
                self.nodes.pop(i)
                if i == self.size-2:
                    self.nodes.insert(i, Node(self.canvas, d[0], d[1], d[2], d[3], d[4], temp_data, d[5], False))
                else:
                    self.nodes.insert(i, Node(self.canvas, d[0], d[1], d[2], d[3], d[4], temp_data, d[5], True))

            self.nodes[-1].remove_arrow()
            self.nodes[self.size-1].delete_node()

            self.nodes.pop(self.size-1)
            self.canvas.delete(self.index_canvas[-1])
            self.index_canvas.pop()
            self.size -= 1
        print(self.nodes, self.size)


if __name__ == '__main__':
    window = tkinter.Tk()
    SCREEN_WIDTH = window.winfo_screenwidth()
    SCREEN_HEIGHT = window.winfo_screenheight()
    window.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
    canvas = tkinter.Canvas(window, width=int(0.6 * SCREEN_WIDTH), height=SCREEN_HEIGHT, bg='#ffee38')

    l = LinkedList(canvas, window)
    # ---------Frame-------------
    frame = tkinter.Frame(window, width=int(0.4 * SCREEN_WIDTH), height=SCREEN_HEIGHT, bg='#b2e49c')
    entry_var = tkinter.StringVar()
    insert_index = tkinter.IntVar()
    insert_button = tkinter.Button(frame, text='Insert', font=('Courier', 15, 'normal'),
                                 command=lambda: l.insert(entry_var.get(), insert_index.get()))
    insert_entry = tkinter.Entry(frame, textvariable=entry_var, font=('Forte', 15), width=14)
    at_index_label = tkinter.Label(frame, text='at index:', font=('Courier', 15, 'normal'))
    insert_index_entry = tkinter.Entry(frame, textvariable=insert_index, font=('Forte', 15), width=5)

    remove_index = tkinter.IntVar()
    remove_button = tkinter.Button(frame, text='Remove', font=('Courier', 15, 'normal'), command=lambda: l.remove(remove_index.get()))
    remove_label = tkinter.Label(frame, text='Node at index', font=('Courier', 15, 'normal'))
    remove_entry = tkinter.Entry(frame, textvariable=remove_index, font=('Forte', 15), width=5)

    insert_button.place(x=50, y=550)
    insert_entry.place(x=150, y=550)
    at_index_label.place(x=320, y=550)
    insert_index_entry.place(x=450, y=550)
    remove_button.place(x=50, y=650)
    remove_label.place(x=150, y=650)
    remove_entry.place(x=320, y=650)
    # --------------------------
    canvas.place(x=0, y=0)
    frame.place(x=int(0.6*SCREEN_WIDTH), y=0)
    window.mainloop()
