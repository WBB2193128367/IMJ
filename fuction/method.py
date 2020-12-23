import requests
from PIL import Image, ImageTk
import tkinter.filedialog
from tkinter import messagebox
import threading


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
            with open(savepath + "//" + "1.jpg", 'wb') as out:
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
            with open(savepath + "//" + "1.jpg", 'wb') as out:
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
    im = Image.open(filename).resize((width, height))
    return ImageTk.PhotoImage(im)


def liulan(str4):
    m = tkinter.filedialog.askdirectory()
    str4.set(m)
    return m


def liulan1(str4):
    m = tkinter.filedialog.askopenfilename()
    str4.set(m)
    return m
