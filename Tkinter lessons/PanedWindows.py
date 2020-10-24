from tkinter import *

root = Tk()
root.title("Paned Windows")
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")
root.geometry("400x400")

#create panel
panel_1 = PanedWindow(root, bd=4, relief="raised", bg="red")
panel_1.pack(fill=BOTH, expand=1)
left_label = Label(panel_1, text="LEFT")
panel_1.add(left_label)

#second panel
panel_2 = PanedWindow(panel_1, orient=VERTICAL, bd=4, relief="raised", bg="blue")
panel_1.add(panel_2)
top_label = Label(panel_2, text="TOP")
panel_2.add(top_label)
bottom_label = Label(panel_2, text="BOTTOM")
panel_2.add(bottom_label)

root.mainloop()