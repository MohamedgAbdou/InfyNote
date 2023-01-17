from tkinter import *

root = Tk()
root.geometry("+500+200")
root.title("Note App")
root.attributes("-topmost", True) # keep the window on top of all other windows

notes = []

def on_submit():
    note = note_entry.get()
    if note:
        note_frame = Frame(root)
        note_frame.pack()
        note_label = Label(note_frame, text=note, fg='red')
        note_label.pack(side=LEFT)
        check_button = Button(note_frame, text="Check", command=lambda: check_and_destroy(note_frame))
        check_button.pack(side=LEFT)
        notes.append(note_frame)
        note_entry.delete(0, END)

def check_and_destroy(note_frame):
    note_frame.destroy()
    notes.remove(note_frame)
    if not notes:
        exit_button.config(state=NORMAL)

note_entry = Entry(root)
note_entry.pack()

submit_button = Button(root, text="Submit", command=on_submit)
submit_button.pack()

exit_button = Button(root, text="Exit", command=root.destroy, state=DISABLED)
exit_button.pack()

root.mainloop()
