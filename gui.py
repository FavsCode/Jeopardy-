import tkinter as tk

root = tk.Tk()

# Setting the window properties

root.title('Jeopardy! in Python')
root.configure(background='#060ce9')
root.state('zoomed')

# Adding the headers

root.rowconfigure(0, weight=1) # Configuring the header row beforehand

for i in range(6):
    # Stretch the grid into proportion by ensuring all extra column space is allocated to the widgets
    root.columnconfigure(i, weight=1)

    label = tk.Label(
        root, 
        background='#060ce9', 
        borderwidth=4, 
        relief='solid', 
        font= ('Bahnschrift SemiBold Condensed', 35), 
        fg='#D9D9D9',
        text=i+1
    )
    label.grid(row=0, column=i, sticky='nsew')

# Making the grid and the labels

for row in range(1, 6): # Starting on row 1! (0, 1, 2...)
    # Stretch the grid into proportion by ensuring all extra column space is allocated to the widgets
    root.rowconfigure(row, weight=1)
    for column in range(6): 
        label = tk.Label(
                root, 
                background='#060ce9', 
                borderwidth=3, 
                relief='solid', 
                font=('Bahnschrift SemiBold Condensed', 70, 'bold'),
                fg='#E1B530',
                text=f'${(row)*200}' # So row 0 is $200 and so on...
            )
        label.grid(row=row, column=column, sticky='nsew')

root.mainloop()
