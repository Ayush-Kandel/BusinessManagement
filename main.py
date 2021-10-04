from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

root = Tk()
root.title("Business Management System")

width = 1024
height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg='#e5e7e9')

# VARIABLES
USERNAME = StringVar()
PASSWORD = StringVar()
PRODUCT_NAME = StringVar()
PRODUCT_PRICE = IntVar()
PRODUCT_QTY = IntVar()
SEARCH = StringVar()


# FUNCTIONS


# EXIT
def Exit():
    result = tkMessageBox.askquestion('Business Management system', 'Are you sure you want to exit?',icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def Exit2():
    result = tkMessageBox.askquestion('Business Management System', 'Are you sure you want to exit?',icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()



# LOGIN
def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Business Management Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()




# LOGIN2
def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Business Admin Log-In", font=('Segoe UI', 18,'bold'), width=600, bg='#1877f2',
                     fg='#ffffff')
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:", font=('Segoe UI', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('Segoe UI', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('Segoe UI', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('Segoe UI', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('Segoe UI', 25), width=15, show="*")
    password.grid(row=1, column=1)


# Button for login
    btn_login = Button(MidLoginForm, text="Login", font=('Segoe UI', 18, 'bold'), width=30,bg='#1877f2',fg='white',bd=2, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)




def Home():
    global Home
    Home = Tk()
    Home.title("Business Management System/home")
    width = 1024
    height = 720
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Business Inventory", font=('Segoe UI', 35, 'underline', 'bold'))
    lbl_display.pack()

    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit2)
    menubar.add_cascade(label="Account", menu=filemenu)
    Home.config(menu=menubar)
    Home.config(bg="#ffffff")

    #BUTTONS IN HOMEPAGE
    btn_addnew = Button(Title, font=('Segoe UI', 14, 'bold'), width='20', height='4', bd='2', text='Add New Product',
                        bg='#1877f2',fg='white', command=lambda: ShowAddNew())
    btn_addnew.pack(side=TOP, padx=40, pady=30, fill=X)


    btn_view =  Button(Title, font=('Segoe UI', 14, 'bold'), width='20', height='4', bd='2', text='View Products',
                       bg='light green',fg='white', command=lambda: ShowView())
    btn_view.pack(side=TOP, padx=40, pady=30, fill=X)


    btn_sale = Button(Title, font=('Segoe UI', 14, 'bold'), width='20', height='4', bd='2', text='Scale Products',
                      bg='grey',fg='white', command=lambda: ShowSale())
    btn_sale.pack(side=BOTTOM, padx=40, pady=30, fill=X)



def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Business Inventory/Add new")
    width = 600
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()


def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Product", font=('Segoe UI', 18), width=600,bg='#1877f2',fg='white')
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    lbl_productname = Label(MidAddNew, text="Product Name:", font=('Segoe UI', 25), bd=10)
    lbl_productname.grid(row=0, sticky=W)
    lbl_qty = Label(MidAddNew, text="Product Quantity:", font=('Segoe UI', 25), bd=10)
    lbl_qty.grid(row=1, sticky=W)
    lbl_price = Label(MidAddNew, text="Product Price:", font=('Segoe UI', 25), bd=10)
    lbl_price.grid(row=2, sticky=W)
    productname = Entry(MidAddNew, textvariable=PRODUCT_NAME, font=('Segoe UI', 25), width=15)
    productname.grid(row=0, column=1)
    productqty = Entry(MidAddNew, textvariable=PRODUCT_QTY, font=('Segoe UI', 25), width=15)
    productqty.grid(row=1, column=1)
    productprice = Entry(MidAddNew, textvariable=PRODUCT_PRICE, font=('Segoe UI', 25), width=15)
    productprice.grid(row=2, column=1)

    # SAVE BUTTON
    btn_add = Button(MidAddNew, text="Save", font=('Segoe UI', 18), width=30, bg="#009ACD", command=AddNew)
    btn_add.grid(row=3, columnspan=2, pady=20)


def AddNew():
    Database()
    cursor.execute("SELECT * FROM `product` WHERE `product_name` = '%s'" % str(PRODUCT_NAME.get()))
    arr = cursor.fetchone()
    if arr is None:
        cursor.execute("INSERT INTO `product` (product_name, product_qty, product_price) VALUES(?, ?, ?)",
                       (str(PRODUCT_NAME.get()), int(PRODUCT_QTY.get()), int(PRODUCT_PRICE.get())))
    else:
        cursor.execute(
            "UPDATE `product` SET `product_name` = ?, `product_qty` = ?, `product_price` = ? WHERE `product_id` = ?",
            (str(arr[1]), int(arr[2]) + int(PRODUCT_QTY.get()), int(PRODUCT_PRICE.get()), int(arr[0])))
    conn.commit()
    PRODUCT_NAME.set("")
    PRODUCT_PRICE.set("")
    PRODUCT_QTY.set("")
    cursor.close()
    conn.close()


def ViewForm():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Products", font=('Segoe UI', 18), width=600,bg='#1877f2',fg='white')
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('Segoe UI', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('Segoe UI', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Refresh", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", fg= 'black', bg='red', command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("ProductID", "Product Name", "Product Qty", "Product Price"), selectmode="extended",
                        height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('ProductID', text="ProductID", anchor=W)
    tree.heading('Product Name', text="Product Name", anchor=W)
    tree.heading('Product Qty', text="Product Qty", anchor=W)
    tree.heading('Product Price', text="Product Price", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()


def SaleForm():
    global tree2
    global lbl_tot
    FlushSales()
    TopViewForm = Frame(saleform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(saleform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(saleform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="Sale", font=('Segoe UI', 18), width=600,bg='#1877f2',fg='white')
    lbl_text.pack(fill=X)
    btn_search = Button(LeftViewForm, text="Add Item", command=ShowAddItem)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Delete", command=DeleteSale, bg='red',fg='black')
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    lbl_tot = Label(LeftViewForm, text="Total Amount = 0", font=('Segoe UI', 10), width=20)
    lbl_tot.pack(side=TOP, padx=10, pady=10)
    btn_delete = Button(LeftViewForm, text="Paid", command=Paid)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree2 = ttk.Treeview(MidViewForm, columns=("ProductID", "Product Name", "Product Qty", "Product Price", "Total"),
                         selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                         xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree2.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree2.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree2.heading('ProductID', text="ProductID", anchor=W)
    tree2.heading('Product Name', text="Product Name", anchor=W)
    tree2.heading('Product Qty', text="Product Qty", anchor=W)
    tree2.heading('Product Price', text="Product Price", anchor=W)
    tree2.heading('Total', text="Total", anchor=W)
    tree2.column('#0', stretch=NO, minwidth=0, width=0)
    tree2.column('#1', stretch=NO, minwidth=0, width=0)
    tree2.column('#2', stretch=NO, minwidth=0, width=150)
    tree2.column('#3', stretch=NO, minwidth=0, width=110)
    tree2.column('#4', stretch=NO, minwidth=0, width=110)
    tree2.column('#5', stretch=NO, minwidth=0, width=70)
    tree2.pack()


def ShowAddItem():
    global additemform
    additemform = Toplevel()
    additemform.title("Business Inventory/Add Item")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (3 * (width / 2))
    y = (screen_height / 2) - (height / 2)
    additemform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    additemform.resizable(0, 0)
    AddItemForm()


def AddItemForm():
    global lbl_alrt
    TopAddItem = Frame(additemform, width=600, height=100, bd=1, relief=SOLID)
    TopAddItem.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddItem, text="Add New Item", font=('Segoe UI', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddItem = Frame(additemform, width=600)
    MidAddItem.pack(side=TOP, pady=50)
    lbl_productname = Label(MidAddItem, text="Product Name:", font=('Segoe UI', 25), bd=10)
    lbl_productname.grid(row=0, sticky=W)
    lbl_qty = Label(MidAddItem, text="Product Quantity:", font=('Segoe UI', 25), bd=10)
    lbl_qty.grid(row=1, sticky=W)
    productname = Entry(MidAddItem, textvariable=PRODUCT_NAME, font=('Segoe UI', 25), width=15)
    productname.grid(row=0, column=1)
    productqty = Entry(MidAddItem, textvariable=PRODUCT_QTY, font=('Segoe UI', 25), width=15)
    productqty.grid(row=1, column=1)
    btn_add = Button(MidAddItem, text="Add Item", font=('Segoe UI', 18), width=30, bg="#009ACD", command=AddItem)
    btn_add.grid(row=2, columnspan=2, pady=20)
    lbl_alrt = Label(MidAddItem, text="", font=('Segoe UI', 18))
    lbl_alrt.grid(row=3, columnspan=2)


def AddItem():
    Database()
    cursor.execute("SELECT * FROM `product` WHERE `product_name` = '%s'" % str(PRODUCT_NAME.get()))
    arr = cursor.fetchone()
    cursor.execute("SELECT * FROM `sale` WHERE `name` = '%s'" % str(PRODUCT_NAME.get()))
    arr1 = cursor.fetchone()
    x = 0
    if arr1 is not None:
        x = int(arr[2])
    if arr is None:
        lbl_alrt.config(text="Item not in inventory", fg="red")
    elif int(arr[2]) < (int(PRODUCT_QTY.get()) + x):
        lbl_alrt.config(text="Insufficient no. of units", fg="red")
    else:
        lbl_alrt.config(text="")
        total = int(PRODUCT_QTY.get()) * int(arr[3])
        if arr1 is None:
            cursor.execute("INSERT INTO `sale` (p_id, name, quantity, price_per_unit, total) VALUES(?, ?, ?, ?, ?)",
                           (int(arr[0]), str(PRODUCT_NAME.get()), str(PRODUCT_QTY.get()), str(arr[3]), str(total)))
        else:
            cursor.execute("UPDATE `sale` SET `quantity` = ?, total = ? WHERE `name` = ?",
                           ((int(arr1[2]) + int(PRODUCT_QTY.get())), (total + int(arr1[4])), str(PRODUCT_NAME.get())))
        lbl_tot.config(text="Total Price = %d" % CalcTotal())
    conn.commit()
    tree2.delete(*tree2.get_children())
    DisplayData2()
    PRODUCT_NAME.set("")
    PRODUCT_PRICE.set("")
    PRODUCT_QTY.set("")


def CalcTotal():
    cursor.execute("SELECT * FROM `sale`")
    t = cursor.fetchall()
    tot = 0
    for r in t:
        tot = tot + int(r[4])
    return tot


def DeleteSale():
    if not tree2.selection():
        print("ERROR")
    else:
        curItem = tree2.focus()
        contents = (tree2.item(curItem))
        selecteditem = contents['values']
        tree2.delete(curItem)
        Database()
        cursor.execute("DELETE FROM `sale` WHERE `p_id` = %d" % selecteditem[0])
        lbl_tot.config(text="Total Price = %d" % CalcTotal())
        conn.commit()
        cursor.close()
        conn.close()


def Paid():
    Database()
    cursor.execute("SELECT * FROM `sale`")
    t = cursor.fetchall()
    for r in t:
        cursor.execute("SELECT * FROM `product` WHERE product_id = %d" % r[0])
        ir = cursor.fetchone()
        if int(ir[2]) == int(r[2]):
            cursor.execute("DELETE FROM `product` WHERE `product_id` = %d" % ir[0])
        else:
            cursor.execute(
                "UPDATE `product` SET `product_qty` = '%s' WHERE `product_id` = %d" % ((int(ir[2]) - int(r[2])), r[0]))
    conn.commit()
    lbl_tot.config(text="Total Price = 0")
    tree2.delete(*tree2.get_children())
    FlushSales()


def FlushSales():
    Database()
    cursor.execute("DELETE FROM `sale`")
    conn.commit()
    cursor.close()
    conn.close()


def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def DisplayData2():
    Database()
    cursor.execute("SELECT * FROM `sale`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree2.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `product` WHERE `product_name` LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()


def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")


def Delete():
    if not tree.selection():
        print("ERROR")
    else:
        result = tkMessageBox.askquestion('Business Inventory', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `product` WHERE `product_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("Business Inventory/View Product")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm()


def ShowSale():
    global saleform
    saleform = Toplevel()
    saleform.title("Business Inventory/Sale")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    saleform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    saleform.resizable(0, 0)
    SaleForm()


def Logout():
    result = tkMessageBox.askquestion('Business Inventory', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        admin_id = ""
        root.deiconify()
        Home.destroy()


def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()


def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()

# DATABASE
def Database():
    global conn, cursor
    conn = sqlite3.connect("business.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `sale` (p_id INTEGER, name TEXT, quantity TEXT, price_per_unit TEXT, total TEXT)")
    cursor.execute("SELECT * FROM `admin`")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()

# MENUBAR WIDGETS
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)


# LOGIN BUTTON
btn_login = Button(root, text="Click To Proceed", font=('Segoe UI', 18, 'bold'), width=30, bg="#009ACD",bd=7,fg='white', command=ShowLoginForm)
btn_login.grid(row=40, columnspan=50, pady=250, padx = 300)



# LABEL for Welcome to GARUDA
lbl_text = Label(root, text="Welcome ", font=('Open Sans', 28), bg='#e5e7e9', fg='black')
lbl_text.grid(row= 10, columnspan=50, pady=10)
lbl_text = Label(root, text="To", font=('Open Sans', 28), bg='#e5e7e9', fg='black')
lbl_text.grid(row=11, columnspan=50, pady=10)
lbl_text = Label(root, text="Business Management", font=('Open Sans', 40, 'bold'), bg='#e5e7e9', fg='#1877f2')
lbl_text.grid(row= 12, columnspan=50, pady=10)




# INITIALIZATION
if __name__ == '__main__':
    root.mainloop()


