import tkinter as tk

root = tk.Tk()

# Setting the window properties
root.title('Jeopardy! in Python')
root.configure(background='#060ce9')
root.state('zoomed')

# Adding the headers
for i in range(1, 7):
    # Stretch the header into proportion by ensuring all extra space is allocated to the widgets
    root.columnconfigure(i-1, weight=1)

    label = tk.Label(
        root, 
        background='#060ce9', 
        borderwidth=5, 
        relief='solid', 
        font= ('Swiss 911', 12), 
        text=i
    )
    label.grid(row=0, column=i-1, sticky='nsew')

root.mainloop()