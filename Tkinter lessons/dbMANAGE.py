from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Database")
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")
root.geometry("400x400")

#Database
#create a database or open
conn = sqlite3.connect('address_book.db')
#create cursor
cur = conn.cursor()

#create table
cur.execute(""" CREATE TABLE IF NOT EXISTS addresses(
first_name text,
last_name text,
address text,
city text,
state text,
zip_code integer
)""")

#function to update databasae
def update():
    # create a database or open
    conn = sqlite3.connect('address_book.db')
    # create cursor
    cur = conn.cursor()

    rec_id = select_box.get()
    cur.execute(""" UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zip_code = :zipcode
     
        WHERE oid = """ + rec_id,
                {
                    'first': f_name_editor.get(),
                    'last': l_name_editor.get(),
                    'address': address_editor.get(),
                    'city': city_editor.get(),
                    'state': state_editor.get(),
                    'zipcode': zipcode_editor.get()
                })

    # commit changes
    conn.commit()
    # close connection
    conn.close()

    editor.destroy()



# edit fuction to update button
def edit():
    global editor
    editor = Tk()
    editor.title("Edit Box")
    editor.iconbitmap("C:/Users/messi/Downloads/favicon.ico")
    editor.geometry("400x400")
    # create a database or open
    conn = sqlite3.connect('address_book.db')
    # create cursor
    cur = conn.cursor()

    record_id = select_box.get()
    # query the database
    cur.execute("SELECT * FROM addresses WHERE oid = " + record_id)  # oid is primary key
    records = cur.fetchall()

    #setting values of editor as global to accessed anywhere
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # create entry box
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)
    # create labels
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text="Zip Code")
    zipcode_label_editor.grid(row=5, column=0)

    # create a SAVE button to save dited record
    save_button = Button(editor, text="Save", command=update)
    save_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    # loop through records
    print(records)
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

# function to delete item
def delete():
    # create a database or open
    conn = sqlite3.connect('address_book.db')
    # create cursor
    cur = conn.cursor()

    #delete record
    cur.execute("DELETE FROM addresses WHERE oid = " + select_box.get())


    # commit changes
    conn.commit()
    # close connection
    conn.close()

#submit function for data base
def submit():
    # create a database or open
    conn = sqlite3.connect('address_book.db')
    # create cursor
    cur = conn.cursor()

    #insert into table
    cur.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                {
                    'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state': state.get(),
                    'zipcode': zipcode.get()
                })

    # commit changes
    conn.commit()
    # close connection
    conn.close()



    #clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    address.delete(0, END)
    zipcode.delete(0, END)
    return

#create query function
def query():
    # create a database or open
    conn = sqlite3.connect('address_book.db')
    # create cursor
    cur = conn.cursor()

    #query the database
    cur.execute("SELECT *,oid FROM addresses") #oid is primary key
    records = cur.fetchall()
    #print(records)
    #loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " \t" + str(record[6]) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)
    # commit changes
    conn.commit()
    # close connection
    conn.close()
    return

#create entry box
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

select_box = Entry(root, width=30)
select_box.grid(row=8, column=1, padx=20, pady=5)

#create labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zip Code")
zipcode_label.grid(row=5, column=0)

select_label = Label(root, text="Select ID")
select_label.grid(row=8, column=0, pady=5)

#create submit button
submit_button = Button(root, text="Submit Entry", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#create a query button
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#create a DELETE button
delete_button = Button(root, text="Delete Record", command=delete)
delete_button.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#create a update button
update_button = Button(root, text="Edit Record", command=edit)
update_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#commit changes
conn.commit()
#close connection
conn.close()

root.mainloop()