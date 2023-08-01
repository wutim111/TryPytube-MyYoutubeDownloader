from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
import os




def Button_Event (type:str):
    Dir_path='./YT下載器'
    address=entry.get()
    
    try:
        yt=YouTube(address)
    except:
        messagebox.showerror('下載失敗' ,'下載發生錯誤,請檢察網址')
    if YouTube(address).title !='' :
        Dir_path+='/'+yt.title
        if type=='mp4' :
            fileName=Dir_path+'/'+yt.title+'.mp4'
            if os.path.isfile(fileName):
                messagebox.showinfo('請檢察一下','請檢察當前資料夾中該檔案是否已存在')
                return
            yt.streams.get_highest_resolution().download(output_path=Dir_path)
        elif type=='mp3':
            ReName=0
            fileName=Dir_path+'/'+yt.title
            if os.path.isfile(fileName+'.mp3'):
                messagebox.showinfo('請檢察一下','請檢察當前資料夾中該檔案是否已存在')
                return
            if os.path.isfile(fileName+'.mp4'):
                os.rename(fileName+'.mp4',fileName+'1.mp4')
                ReName=1
            out_file= yt.streams.get_audio_only().download(output_path=Dir_path)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            if ReName==1:
                 os.rename(fileName+'1.mp4',fileName+'.mp4')
        messagebox.showinfo('下載成功',yt.title+'.'+type+' 下載成功'+'\n'+'請注意 YT下載器 資料夾')
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
             command=lambda: Button_Event('mp4'))
B2=tk.Button(root,text='下載成MP3',relief="ridge",
            activebackground='#BE77FF',#設定滑鼠位於按鈕時的背景顏色
            activeforeground='#FFFFFF',#設定滑鼠位於按鈕時的前景顏色
             command=lambda: Button_Event('mp3'))
entry = tk.Entry(root)  # 放入單行輸入框


text.pack()
entry.pack()
B1.pack()
B2.pack()
root.mainloop()