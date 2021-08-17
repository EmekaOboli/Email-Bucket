from tkinter import *
import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/EmailBucket")
def root_build():    
    root = Tk()
    root.title("{Lawplug}")
    root.geometry("500x500")
    root.iconbitmap("C:/Users/emeka/Downloads/lawplugfavicon.ico")
    
    conn = sqlite3.connect("Newsletter_Email_Locker.db")  
    cur = conn.cursor()
    
    # cur.execute("CREATE TABLE email_List(emails TEXT)")
    
    emeka_txt = Label(root, text="EmailBucket" , fg='purple' )
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


#update button 
    update_button = Button(root, text ="Submit email!", fg="purple", bg="white", width=15, command=insert_db)
    update_button.pack()

# commit to memory in database
    conn.commit()
    
    # conn.close()
    
    root.mainloop()

if __name__ == '__main__':
    app.run()


