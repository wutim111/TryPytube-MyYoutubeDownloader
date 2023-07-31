from pytube import YouTube
import tkinter as tk
from tkinter import messagebox



def VideoButton_Event():
    address=entry.get()
    
    try:
        yt=YouTube(address)
    except:
        messagebox.showerror('下載失敗' ,'下載發生錯誤,請檢察網址')
    if YouTube(address).title !='' :
        messagebox.showinfo('下載成功',yt.title+'.mp4 正在下載中')
        yt.streams.get_highest_resolution().download()
    else :
        messagebox.showerror('下載失敗' ,'下載發生錯誤,請檢察網址')


def MusicButton_Event():
    address=entry.get()
    try:
        yt=YouTube(address)
    except:
        messagebox.showerror('下載失敗' ,'下載發生錯誤,請檢察網址')
    if YouTube(address).title !='' :
        messagebox.showinfo('下載成功',yt.title+'.mp3 正在下載中')
        yt.streams.get_audio_only().download()
    else :
        messagebox.showerror('下載失敗' ,'下載發生錯誤,請檢察網址')
root = tk.Tk()
root.geometry("250x100+200+300")
root.title('YT下載器')
text=tk.Label(root, text='網址') #建立標籤

B1=tk.Button(root,text='下載成MP4',relief="ridge",
            activebackground='#BE77FF',#設定滑鼠位於按鈕時的背景顏色
            activeforeground='#FFFFFF',#設定滑鼠位於按鈕時的前景顏色
             command=VideoButton_Event)
B2=tk.Button(root,text='下載成MP3',relief="ridge",
            activebackground='#BE77FF',#設定滑鼠位於按鈕時的背景顏色
            activeforeground='#FFFFFF',#設定滑鼠位於按鈕時的前景顏色
             command=MusicButton_Event)
entry = tk.Entry(root)  # 放入單行輸入框


text.pack()
entry.pack()
B1.pack()
B2.pack()
root.mainloop()