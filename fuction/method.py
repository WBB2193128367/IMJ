from tkinter import *
import requests
from PIL import Image, ImageTk
import tkinter.filedialog
from tkinter import messagebox
import threading
import time

def thread(imagepath, savepath, xuanze):
    t = threading.Thread(target=method, args=(imagepath, savepath, xuanze,))
    # 设置守护线程，进程退出不用等待子线程完成
    t.setDaemon(True)
    t.start()


def method(imagepath, savepath, xuanze):
    if xuanze == '本地图片' and imagepath != "" and savepath != "" and imagepath.startswith(
            "http") == False:

        # 对本地的图片进行抠图
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(imagepath, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': '9oEfkNXs2SoX1Ktbktx9GRpe'},
        )
        if response.status_code == requests.codes.ok:
            with open(savepath + "/" + time1()+imagepath[-4:], 'wb') as out:
                out.write(response.content)
            tkinter.messagebox.showinfo('提示!', '抠图成功！')
        else:
            tkinter.messagebox.showinfo('提示!', '抠图失败！')
    elif xuanze == "网络图片" and imagepath != "" and savepath != "" and imagepath.startswith("http"):
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            data={
                'image_url': imagepath,
                'size': 'auto'
            },
            headers={'X-Api-Key': '9oEfkNXs2SoX1Ktbktx9GRpe'},
        )
        if response.status_code == requests.codes.ok:
            with open(savepath + "/" + time1()+imagepath[-4:], 'wb') as out:
                out.write(response.content)
            tkinter.messagebox.showinfo('提示!', '抠图成功！')
        else:
            tkinter.messagebox.showinfo('提示!', '抠图失败！')
    elif imagepath == "" or savepath == "":
        tkinter.messagebox.showinfo('警告!', '文本框不能为空！！！')
    elif xuanze == '本地图片' and imagepath != "" and savepath != "" and imagepath.startswith(
            "http"):
        tkinter.messagebox.showinfo('警告!', '你输入的不是本地图片噢！')
    elif xuanze == '网络图片' and imagepath != "" and savepath != "" and imagepath.startswith(
            "http") == False:
        tkinter.messagebox.showinfo('警告!', '你输入的不是网络图片噢！')


def get_image(filename, width, height):
    im =Image.open(filename).resize((width, height))
    return ImageTk.PhotoImage(im)


def liulan(str4):
    m = tkinter.filedialog.askdirectory()
    str4.set(m)
    #return m


def liulan1(str4):
    m = tkinter.filedialog.askopenfilename()
    str4.set(m)
    #return m

def guanyu():
    tkinter.messagebox.showinfo('提示', '该软件由WBB开发，仅供学习使用，请勿用作商用！！！')


def print_selection(root,v):
    root.attributes("-alpha",1-v)


# def toumingdu(root):
#     top1 = Toplevel()  # 创建弹出式窗体
#     top1.title('设置页面')
#     top1.geometry("250x100+800+280")
#     entry = Entry(top1)
#     entry.place(x=10, y=10)
#     btn = Button(
#         top1,
#         text="确认",
#         bd=8,
#         cursor='pirate',
#         relief="raised",
#         fg='black',
#         width=5,
#         height=1,
#         compound=tkinter.CENTER,
#         command=lambda :print_selection(root,entry.get(),top1))
#     btn.place(x=30, y=40)
#     top1.mainloop()
def toumingdu(root):
    top1 = Toplevel()  # 创建弹出式窗体
    top1.title('设置页面')
    top1.geometry("250x100+800+280")
    top1.resizable(0, 0)
    lb = Label(top1, text="清晰")
    lb.place(x=18, y=10)
    lb1 = Label(top1, text="模糊")
    lb1.place(x=205, y=10)
    S = Scale(
        top1,
        from_=0,
        to=1,
        resolution=0.1,
        showvalue=0,
        orient=HORIZONTAL,
        length=150)
    S.place(x=50, y=10)
    btn = Button(
        top1,
        text="确认",
        bd=8,
        cursor='pirate',
        relief="raised",
        fg='black',
        width=5,
        height=1,
        compound=tkinter.CENTER,
        command=lambda :print_selection(root,S.get()))
    btn.place(x=98, y=50)
    top1.mainloop()
def time1():
    s=time.strftime('%Y-%m-%d%H%M%S',time.localtime())
    return s
