## Main Working

import tkinter
from linked_list import LinkedList
from arrayDs import ArrayDs
from stack import Stack
from queue import Queue
from tree import Tree


def clear_frame():
    global frame
    frame.destroy()


def set_frame():
    global frame, option_dropdown, ds_label
    frame = tkinter.Frame(window, bg='#17ea74', width=SCREEN_WIDTH - CANVAS_WIDTH, height=SCREEN_HEIGHT)
    option_dropdown = tkinter.OptionMenu(frame, selected_option, *options, command=change_ds)
    option_dropdown.config(font=('Bahnschrift Condensed', 15, 'normal'), width=15)
    ds_label = tkinter.Label(frame, text='Data Structure', font=('Bookman Old Style', 20, 'normal'))

    ds_label.place(x=70, y=50)
    option_dropdown.place(x=310, y=50)
    frame.place(x=CANVAS_WIDTH, y=0)


def is_empty(obj, empty_var):
    empty_var.set('Yes' if obj.is_empty() else 'No')


# To change the DS
def change_ds(ds):
    clear_frame()
    canvas.delete('all')
    set_frame()
    if ds == 'Stack':
        s = Stack(canvas, window)

        text = tkinter.StringVar()
        push_entry = tkinter.Entry(frame, textvariable=text, font=('Baskerville Old Face', 19, 'normal'), width=17)
        push_button = tkinter.Button(frame, text='Push', font=BUTTON_FONT, command=lambda: s.push(push_entry.get()))
        pop_button = tkinter.Button(frame, text='Pop', font=BUTTON_FONT, command=s.pop)
        peek_button = tkinter.Button(frame, text='Peek', font=BUTTON_FONT, command=s.peek)
        empty = tkinter.StringVar()
        is_empty_label = tkinter.Label(frame, textvariable=empty, font=('Baskerville Old Face', 20, 'normal'), width=10)
        is_empty_button = tkinter.Button(frame, text='Is Empty?', font=BUTTON_FONT, command=lambda: is_empty(s, empty))
        expression = tkinter.StringVar()
        postfix_label = tkinter.Label(frame, text='Enter Postfix', font=('Baskerville Old Face', 20, 'normal'))
        postfix_entry = tkinter.Entry(frame, textvariable=expression, font=('Baskerville Old Face', 19, 'normal'), width=20)
        done_button = tkinter.Button(frame, text="Evaluate", font=BUTTON_FONT,
                                     command=lambda: s.evaluate(expression.get()))

        postfix_label.place(x=80, y=350)
        postfix_entry.place(x=80, y=400)
        done_button.place(x=340, y=400)
        push_entry.place(x=50, y=502)
        push_button.place(x=270, y=500)
        pop_button.place(x=50, y=550)
        peek_button.place(x=50, y=600)
        is_empty_button.place(x=50, y=650)
        is_empty_label.place(x=165, y=650)

    elif ds == 'Queue':
        q = Queue(canvas, window)

        entry_var = tkinter.StringVar()
        enqueue_entry = tkinter.Entry(frame, textvariable=entry_var, font=('Baskerville Old Face', 19, 'normal'), width=17)
        enqueue_button = tkinter.Button(frame, text='Enqueue', font=BUTTON_FONT, width=16,
                                        command=lambda: q.enqueue(entry_var.get()))
        dequeue_button = tkinter.Button(frame, text='Dequeue', font=BUTTON_FONT, width=16, command=q.dequeue)
        first_button = tkinter.Button(frame, text='First', font=BUTTON_FONT, width=16, command=q.first)

        empty = tkinter.StringVar()
        is_empty_label = tkinter.Label(frame, textvariable=empty, font=('Baskerville Old Face', 20, 'normal'), width=10)
        is_empty_button = tkinter.Button(frame, text='Is Empty?', font=BUTTON_FONT, command=lambda: is_empty(q, empty))

        enqueue_entry.place(x=50, y=502)
        enqueue_button.place(x=270, y=500)
        dequeue_button.place(x=50, y=550)
        first_button.place(x=50, y=600)
        is_empty_button.place(x=50, y=650)
        is_empty_label.place(x=165, y=650)
    elif ds == 'Linked List':
        l = LinkedList(canvas, window)
        entry_var = tkinter.StringVar()
        insert_index = tkinter.IntVar()
        insert_button = tkinter.Button(frame, text='Insert', font=BUTTON_FONT,
                                       command=lambda: l.insert(entry_var.get(), insert_index.get()))
        insert_entry = tkinter.Entry(frame, textvariable=entry_var, font=('Baskerville Old Face', 19, 'normal'), width=14)
        at_index_label = tkinter.Label(frame, text='at index:', font=('Baskerville Old Face', 20, 'normal'))
        insert_index_entry = tkinter.Entry(frame, textvariable=insert_index, font=('Baskerville Old Face', 19, 'normal'), width=5)

        remove_index = tkinter.IntVar()
        remove_button = tkinter.Button(frame, text='Remove', font=BUTTON_FONT,
                                       command=lambda: l.remove(remove_index.get()))
        remove_label = tkinter.Label(frame, text='Node at index', font=('Baskerville Old Face', 20, 'normal'))
        remove_entry = tkinter.Entry(frame, textvariable=remove_index, font=('Baskerville Old Face', 19, 'normal'), width=5)

        insert_button.place(x=50, y=550)
        insert_entry.place(x=130, y=550)
        at_index_label.place(x=320, y=550)
        insert_index_entry.place(x=450, y=550)
        remove_button.place(x=50, y=650)
        remove_label.place(x=150, y=650)
        remove_entry.place(x=320, y=650)
    elif ds == 'Array':
        a = ArrayDs(canvas, window)

        capacity_var = tkinter.IntVar()
        cap_entry = tkinter.Entry(frame, textvariable=capacity_var, font=('Baskerville Old Face', 19, 'normal'), width=5)
        make_array_button = tkinter.Button(frame, text='Create Array', font=BUTTON_FONT,
                                           command=lambda: a.create_array(capacity_var.get()))
        of_size_label = tkinter.Label(frame, text='of size', font=('Baskerville Old Face', 20, 'normal'))

        data_var = tkinter.IntVar()
        idx_var = tkinter.IntVar()
        insert_button = tkinter.Button(frame, text='Insert', font=BUTTON_FONT,
                                       command=lambda: a.insert(data_var.get(), idx_var.get()))
        data_entry = tkinter.Entry(frame, textvariable=data_var, font=('Baskerville Old Face', 19, 'normal'), width=7)
        at_label = tkinter.Label(frame, text='at index', font=('Baskerville Old Face', 20, 'normal'))
        idx_entry = tkinter.Entry(frame, textvariable=idx_var, font=('Baskerville Old Face', 19, 'normal'), width=5)

        idx1_var = tkinter.IntVar()
        idx2_var = tkinter.IntVar()
        swap_button = tkinter.Button(frame, text='Swap', font=BUTTON_FONT,
                                     command=lambda: a.swap(idx1_var.get(), idx2_var.get()))
        idx1_entry = tkinter.Entry(frame, textvariable=idx1_var, font=('Baskerville Old Face', 19, 'normal'), width=5)
        idx2_entry = tkinter.Entry(frame, textvariable=idx2_var, font=('Baskerville Old Face', 19, 'normal'), width=5)

        make_array_button.place(x=50, y=550)
        of_size_label.place(x=200, y=550)
        cap_entry.place(x=300, y=550)
        insert_button.place(x=50, y=600)
        data_entry.place(x=130, y=600)
        at_label.place(x=250, y=600)
        idx_entry.place(x=370, y=600)
        swap_button.place(x=50, y=650)
        idx1_entry.place(x=120, y=650)
        idx2_entry.place(x=220, y=650)
    elif ds == 'Tree':
        t = Tree(canvas, window)

        entry_var = tkinter.StringVar()
        root_var = tkinter.StringVar()

        root_entry = tkinter.Entry(frame, textvariable=root_var, font=('Baskerville Old Face', 19, 'normal'), width=16)
        add_root_button = tkinter.Button(frame, text='Add Root', font=BUTTON_FONT, width=16,
                                         command=lambda: t.add_root(root_var.get()))

        value_entry = tkinter.Entry(frame, textvariable=entry_var, font=('Baskerville Old Face', 19, 'normal'), width=16)
        insert_button = tkinter.Button(frame, text='Add child', font=BUTTON_FONT,
                                       command=lambda: t.add_child(entry_var.get()))
        goto_child_button = tkinter.Button(frame, text='Goto Child', font=BUTTON_FONT,
                                           command=t.goto_children)
        next_child_button = tkinter.Button(frame, text='Next Child', font=BUTTON_FONT,
                                           command=t.goto_next_child)
        prev_child_button = tkinter.Button(frame, text='Previous Child', font=BUTTON_FONT,
                                           command=t.goto_prev_child)
        goto_parent_button = tkinter.Button(frame, text='Goto Parent', font=BUTTON_FONT,
                                            command=t.goto_parent)

        root_entry.place(x=50, y=500)
        add_root_button.place(x=260, y=500)
        value_entry.place(x=50, y=550)
        insert_button.place(x=260, y=550)
        goto_child_button.place(x=50, y=600)
        next_child_button.place(x=210, y=600)
        prev_child_button.place(x=380, y=600)
        goto_parent_button.place(x=50, y=650)


window = tkinter.Tk()
SCREEN_WIDTH = window.winfo_screenwidth()
SCREEN_HEIGHT = window.winfo_screenheight() - 70
window.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
window.wm_title('Data Structure Simulator')
CANVAS_WIDTH = int(0.6 * SCREEN_WIDTH)
CANVAS_HEIGHT = SCREEN_HEIGHT

BUTTON_FONT = ('Berlin Sans FB', 15, 'normal')


def start():
    global canvas, selected_option, options
    # -------------Canvas---------------------
    canvas = tkinter.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='#f7ea77')
    canvas.place(x=0, y=0)
    # -----------------------------------

    # -------------Options Frame -----------------------
    selected_option = tkinter.StringVar()
    options = ['Array', 'Linked List', 'Stack', 'Queue', 'Tree']
    set_frame()
    selected_option.set("Array")
    change_ds('Array')


# ------------- Start Screen ----------------------
start_theme = tkinter.PhotoImage(file='images/start_screen.png')
start_img = tkinter.PhotoImage(file='images/s_1.png')
start_canvas = tkinter.Canvas(window, width=start_theme.width(), height=start_theme.height())
start_canvas.create_image(0, 0, anchor='nw', image=start_theme)
start_canvas.place(x=0, y=0)
start_button = tkinter.Button(window, image=start_img, bg='black', font=('Marvel', 20), command=start, borderwidth=3)
start_button.place(x=start_theme.width()-25, y=start_theme.height()//2+20)

window.mainloop()
