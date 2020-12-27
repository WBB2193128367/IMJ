# encoding="utf-8"
from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from fuction import method

root = Tk()  # 创建主窗体
root.title("抠图君")
root.geometry("450x280+750+200")
root.iconbitmap(r'D:\ico\w.ico')
root.resizable(0, 0)

huabu = tkinter.Canvas(root, width=450, height=280)
tupian = method.get_image(r'D:\ico\7.jpg', 450, 280)
huabu.create_image(225, 140, image=tupian)
huabu.pack()


menubar = Menu(root)  # 定义一个菜单栏
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='设置', menu=file)
file.add_command(label='更改透明度', command=lambda: method.toumingdu(root))
menubar.add_cascade(label='关于', command=method.guanyu)
root.config(menu=menubar)






lb = Label(root, text="请选择图片的类型:  ", state='active')
lb.place(x=65, y=70)
combobox = ttk.Combobox(root, width=17, state='readonly')
combobox['values'] = ("本地图片", "网络图片")
combobox.current(1)
combobox.place(x=220, y=70)
lb = Label(root, text="请选择或输入图片的路径:", state='active')
lb.place(x=65, y=100)
str3 = StringVar()
entry = Entry(root, textvariable=str3, width=14)
entry.place(x=220, y=100)
btn2 = Button(
    root,
    text="浏览..",
    width=4,
    height=1,
    cursor='pirate',
    command=lambda: method.liulan1(str3))
btn2.place(x=330, y=96)
lb = Label(root, text="请输入已抠取图的保存位置:", state='active')
lb.place(x=65, y=130)
str4 = StringVar()
entry1 = Entry(root, textvariable=str4, width=14)
entry1.place(x=220, y=130)
btn1 = Button(
    root,
    text="浏览..",
    width=4,
    height=1,
    cursor='pirate',
    command=lambda: method.liulan(str4))
btn1.place(x=330, y=126)
button_image = method.get_image(r'D:\ico\7.jpg', 50, 28)
btn = Button(
    root,
    text="开始抠图",
    image=button_image,
    bd=8,
    cursor='pirate',
    relief="raised",
    fg='black',
    width=50,
    height=28,
    compound=tkinter.CENTER,
    command=lambda: method.thread(entry.get(), entry1.get(), combobox.get()))
btn.place(x=240, y=160)
root.mainloop()
