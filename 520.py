import tkinter as tk
import tkinter.messagebox as messagebox
window = tk.Tk()

window.title('Hello Li Meng Yue')

window.geometry('1600x640')
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='pic.gif')
image = canvas.create_image(250, 0, anchor='n',image=image_file)


l = tk.Label(window, text='Hello, Is is a very nice day to meet you', font=('Arial', 12), )
l.pack()
# TODO:
canvas.place(x=0,y=50,anchor= 'nw')



# canvas.pack()
# image_file = tk.PhotoImage(file='pic.gif')
# image = tk.creat_image(250,0, anchor='n'image=image_file)


tk.Label(window, text='Hello Xiao Jie Jie Wo Guan Cha Ni He Jiu Le.\n Zuo Wo Nv Peng You Hao Ma ?', font=('Arial', 36), ).place(x=400, y=100, anchor='nw')

def on_closing():
        if messagebox.askoko_2o_2cel("Quit", "Do you want to quit?"):
            tk.messagebox.showinfo(title='Quit', message='不要走开哦~')

def Yes_do():

    answer = tk.messagebox.askyesno(title='Chosen',message='Wo Bu Shi Zai Zuo Me Ba, Zhen De Ma ?' )
    print(answer)
    if answer:
        end_answer = tk.messagebox.showinfo(title='Know',message="Wo Ju zhi dao xiao jie jie ni ye xi huan Wo Ya ~ ~")
        print(end_answer)
    else:
        print("NO")
        end_answer = tk.messagebox.showinfo(title='Know',message="Happy 520 :)")
    # tk.Label(window, text='Hello Xiao Jie Jie wo\n', font=('Arial', 36), ).place(x=400, y=200, anchor='nw')

    # tk.Label(window, text='No_2', font=('Arial', 36), ).place(x=400, y=100, anchor='nw')

    # tk.Label(window, text='Hello Xiao Jie Jie wo\n', font=('Arial', 36), ).place(x=400, y=200, anchor='nw')


def No_1():
    sorry.place_forget()
    No_1.place(x=750, y=400, anchor='nw')

def No_2():
    No_1.place_forget()
    No_2.place(x=130, y=320, anchor='nw')

def No_3():
    No_2.place_forget()
    No_3.place(x=630, y=500, anchor='nw')

def No_4():
    No_3.place_forget()
    No_4.place(x=1030, y=320, anchor='nw')

def No_5():
    No_4.place_forget()
    No_5.place(x=430, y=420, anchor='nw')

def No_6():
    No_5.place_forget()
    sorry.place(x=850, y=300, anchor='nw')




yes = tk.Button(window, text='Hao Ya ', font=('Arial', 36), command=Yes_do)
sorry = tk.Button(window, text='Suan le Ba', font=('Arial', 36), command=No_1)

No_1 = tk.Button(window, text='好吃的都给你~', font=('Arial', 36), command=No_2)
No_2 = tk.Button(window, text='好玩的也给你~', font=('Arial', 36), command=No_3)
No_3 = tk.Button(window, text='饭我来做<', font=('Arial', 36), command=No_4)
No_4 = tk.Button(window, text='衣服我洗', font=('Arial', 36), command=No_5)
No_5 = tk.Button(window, text='地我来托QAQ', font=('Arial', 36), command=No_6)




yes.place(x=450, y=300, anchor='nw')
sorry.place(x=850, y=300, anchor='nw')





window.protocol("WM_DELETE_WINDOW", on_closing)




window.mainloop()
