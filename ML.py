import mysql.connector
from sklearn import tree
import tkinter as tk



cnx = mysql.connector.connect(user='root', password='',
                            host='127.0.0.1',
                            database='Craigslist')

cursor = cnx.cursor()

query_string = "SELECT * FROM mytable;"
cursor.execute(query_string)

prices = []
bedrooms = []
spaces = []
areas = []

for (price, bedroom, space, area) in cursor:
    prices.append(price)
    bedrooms.append(bedroom)
    spaces.append(space)
    areas.append(area)


cnx.commit()
cnx.close()


def taking_info_1():
    pe1 = price_entry1.get()
    try:
        pe1_var1 = int(pe1)
    except ValueError:
        result_label1.config(text="Please insert number")

    be1 = bedroom_entry1.get()
    try:
        be1_var2 = int(be1)
    except ValueError:
        result_label1.config(text="Please insert number")
    asked_data= [[pe1_var1, be1_var2]]
    X = []
    y = []
    var1, var2, var3 = prices, bedrooms, areas
    for i in range(len(var1)):
        X.append([var1[i], var2[i]])
        y.append(var3[i])
    train = tree.DecisionTreeClassifier()
    trained = train.fit(X, y)
    answer = trained.predict(asked_data)
    result_label1.config(text=answer[0].replace("(", "").replace(")",""))


    
def taking_info_2():
    pe2 = price_entry2.get()
    try:
        pe2_var1 = int(pe2)
    except ValueError:
        result_label2.config(text="Please insert number")
    se1 = space_entry1.get()
    try:
        se1_var2 = int(se1)
    except ValueError:
        result_label2.config(text="Please insert number")

    asked_data= [[pe2_var1, se1_var2]]

    X = []
    y = []
    var1, var2, var3 = prices, spaces, areas
    for i in range(len(var1)):
        X.append([var1[i], var2[i]])
        y.append(var3[i])
    train = tree.DecisionTreeClassifier()
    trained = train.fit(X, y)
    answer = trained.predict(asked_data)
    result_label2.config(text=answer[0].replace("(", "").replace(")",""))


def taking_info_3():
    se2 = space_entry2.get()
    try:
        se2_var1 = int(se2)
    except ValueError:
        result_label3.config(text="Please insert number")


    be2 = bedroom_entry2.get()
    try:
        be2_var2 = int(be2)
    except ValueError:
        result_label3.config(text="Please insert number")

    asked_data= [[se2_var1, be2_var2]]

    X = []
    y = []
    var1, var2, var3 = spaces, bedrooms, prices
    for i in range(len(var1)):
        X.append([var1[i], var2[i]])
        y.append(var3[i])
    train = tree.DecisionTreeClassifier()
    trained = train.fit(X, y)
    answer = trained.predict(asked_data)
    result_label3.config(text=answer[0])




root = tk.Tk()

root.title("Craigslist")
root.iconbitmap("./web_scraping_craigslist/peace_icon.ico")
root.geometry("1000x150")


# Creating first line
k1, k2 = tk.IntVar(), tk.IntVar()
frame1 = tk.Frame(root, width=50, height=50, bg="red")
frame1.pack(fill=tk.BOTH, expand = True)

price_label1 = tk.Label(frame1, text = "Price:", font=("Arial Bold", 15), bg="red")
price_label1.place(x=10, y=10)

price_entry1 = tk.Entry(frame1, bd=3, textvariable=k1)
price_entry1.place(x=70, y=12)

bedroom_label1 = tk.Label(frame1, text = "Bedroom:", font=("Arial Bold", 15), bg="red")
bedroom_label1.place(x=220, y=10)

bedroom_entry1 = tk.Entry(frame1, bd=3, textvariable=k2)
bedroom_entry1.place(x=320, y=12)

get_location_button1 = tk.Button(frame1, text = "where?", font = ("Arial Bold", 10), command = lambda : taking_info_1())
get_location_button1.place(x=480, y=12)


result_label1 = tk.Label(frame1, text="Empty", font=("Arial Bold", 10), bg="red")
result_label1.place(x=600, y=12)


# Creating second line
k3, k4 = tk.IntVar(), tk.IntVar()
frame2 = tk.Frame(root, width=50, height=50, bg="yellow")
frame2.pack(fill=tk.BOTH, expand = True)

price_label2 = tk.Label(frame2, text = "Price:", font=("Arial Bold", 15), bg="yellow")
price_label2.place(x=10, y=10)

price_entry2 = tk.Entry(frame2, bd=3, textvariable=k3)
price_entry2.place(x=70, y=12)

space_label1 = tk.Label(frame2, text = "Space:", font=("Arial Bold", 15), bg="yellow")
space_label1.place(x=220, y=10)

space_entry1 = tk.Entry(frame2, bd=3, textvariable=k4)
space_entry1.place(x=320, y=12)

get_location_button2 = tk.Button(frame2, text = "where?", font = ("Arial Bold", 10), command = lambda: taking_info_2())
get_location_button2.place(x=480, y=12)


result_label2 = tk.Label(frame2, text="Empty", font=("Arial Bold", 10), bg="yellow")
result_label2.place(x=600, y=12)

# Creating third line
k5, k6 = tk.IntVar(), tk.IntVar()
frame3 = tk.Frame(root, width=50, height=50, bg="blue")
frame3.pack(fill=tk.BOTH, expand = True)

space_label2 = tk.Label(frame3, text = "Space:", font=("Arial Bold", 15), bg="Blue")
space_label2.place(x=10, y=10)

space_entry2 = tk.Entry(frame3, bd=3, textvariable=k5)
space_entry2.place(x=80, y=12)

bedroom_label2 = tk.Label(frame3, text = "Bedroom:", font=("Arial Bold", 15), bg="Blue")
bedroom_label2.place(x=220, y=10)

bedroom_entry2 = tk.Entry(frame3, bd=3, textvariable=k6)
bedroom_entry2.place(x=320, y=12)

get_price_button1 = tk.Button(frame3, text = "how much?", font = ("Arial Bold", 10), command = lambda :taking_info_3())
get_price_button1.place(x=480, y=12)


result_label3 = tk.Label(frame3, text="Empty", font=("Arial Bold", 10), bg="blue")
result_label3.place(x=600, y=12)





root.mainloop()




