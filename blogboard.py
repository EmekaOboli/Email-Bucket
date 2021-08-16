from tkinter import *
import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/blogboard")
def root_build():    
    root = Tk()
    root.title("{Lawplug}")
    root.geometry("500x500")
    root.iconbitmap("C:/Users/emeka/Downloads/lawplugfavicon.ico")
    
    conn = sqlite3.connect("Newsletter_Email_Locker.db")  
    cur = conn.cursor()
    
    # cur.execute("CREATE TABLE email_List(emails TEXT)")
    
    emeka_txt = Label(root, text="BlogBoard" , fg='purple' )
    emeka_txt.pack()

    copyright_txt = Label(root, text='copy right ✒ 2021', fg='purple')
    copyright_txt.pack(side='bottom')

# entry variable
    e = Entry(root, foreground='purple', width=50)
    e.pack()

# label text
    l = Label(root, text="enter your email to get our newsletters" , fg='purple')
    l.pack()

   
# update database with insert
    def insert_db():
        global get_list
        e.get()
        cur.execute("INSERT INTO email_List VALUES (?)", ' ')
        get_list = e.get()
        print(get_list)
        mssg_word= Label(root, text='email saved successfully, check email for newsletters', fg='blue')
        mssg_word.pack()
        conn.commit()
        x = e.clipboard_clear()
        print(x)
        
#keep function for Flask admin 
    # def select_db():
        # cur.execute("SELECT * FROM email_List")
        # y = cur.fetchall()
        # print(y)
        # print (get_list)


#update button 
    update_button = Button(root, text ="Submit email!", fg="purple", bg="white", width=15, command=insert_db)
    update_button.pack()

# dropbox options function
    options = ["good🙂"]
    options1 = ["indifferent😏"]
    options2 = ["bad🙁"]
    options3 = ["no comment🤐"]

    # clicked = IntVar()
    clicked = StringVar()
    clicked.set(options([0])


    def drop_box_ratings():
        label_drop = Label(root, text=clicked.get(),fg="purple", bg="white")
        label_drop.grid(root, column=1, columnspan=6)


    drop_button = OptionMenu(root, clicked, options, options1, options2, options3)
    drop_button.grid(root, column=2)

    drop_button2 = Button(root, text = ' feedback vote', fg="purple", bg="white", command=drop_box_ratings()) 
    drop_button2.grid(root, column=3)

# keep button for Flaskadmin
    # mybutton2 = Button(root, text = "get records", fg="purple", bg="white", width=15, command=select_db)
    # mybutton2.pack()


    # for row in cur.execute("SELECT * FROM email_List"):
        # print(row)
    # conn.fetchall()
    # OR

    # cur.execute(SELETE * oid FROM email_List)
    # records = cur.fetchall()
    # print(records)

    # primary key: oid 
    # usage: "SELECT * oid FROM email_List"
    conn.commit()
    
    # conn.close()
    
    root.mainloop()

if __name__ == '__main__':
    app.run(debug =True, use_reloader=True, port = 80)


