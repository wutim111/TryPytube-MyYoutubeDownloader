from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
import os
import base64

# pyinstaller -F .\YT下載器.py -c --icon=ShiHoIcon.ico -w

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


img='AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAANM1AADTNQAAAAAAAAAAAAD///////////////////////////39/f//////c3Ny/3R0dP9lZWX/UFBQ/19fX/9ra2v/cHBw/2pqav9qamr/aGho/11dXf9XWFj/Xl5e/2NjY/9ubW3/QUNF/1tgZf/s7Ov///////7+/v///////////////////////////////////////////////////////Pz8//////9SVVf/b29v/6enp/+Hh4f/cnJy/3Fxcf91dXX/hoaG/4WFhf+EhIT/enp6/3V1dP9sbGv/ZmZm/3Bvbv9BSVH/NURT/5ueoP//////+/v7/////////////////////////////////////////////v7+///////19fb/lZWV/0FKU/9HS0//VVRU/2ZmZv+vr67/tra2/9PT0v/d3dz/6eno/+Dg4f/j4+L/Z2pu/0hOVP/Qz8//Xl9f/zhDT/9MWWf/YGdv/9XV1f///////v7+////////////////////////////////////////////+/v7///////ExMX/PElW/0NITv/Jycn/YWds/+rq6//h4N//lpeZ/5uco/+ztLX/4eHg//////97goj/WGFq//////8yMjL/HiQr/0lWZP9kbXb/m5yc//Pz8////////v7+//////////////////////////////////39/f//////3t3d/15mbv9KVmP/AAIE/4OBfv9cZW7/KjM7/4SFjf/c4PP/6u7//8/T5P+nqrb/oaKk/2dudP9NVl//gH59/wAAAP9ASVT/P01b/6+vsP//////+Pj5//////////////////////////////////////////////////79/f9dZGr/P05d/05aZ/8NDxH/Jy0y/1VicP8+SVX/xcnX//D0///o7P3/7PD///////94fYn/OEZU/1Febf8fJSv/AQEB/0dTYP9PXWv/QUtV/7q6uv///////f39//////////////////////////////////7+/v//////6uno/0dQW/9TYG//TFlm/0BKVf9SX27/TFln/xseIv8bGxz/rrG+//P3///u8v//vL/N/zg5PP8+SFP/Ul9u/1Ricf8wN0D/PUdS/1Jfbf9RX23/OURP/7Cxsv///////f39//////////////////////////////////3+/v//////Z21z/2Ftev9kbnj/Q09b/2Vxf/9BTVr/AAAA/wAAAP+7v83/7/P///j8//+OkZz/AAAA/xkcIP9PXGr/TVln/01aZ/8/SlX/Slhm/3mDjP9ibnz/RE1X//f29f///////v7+/////////////////////////////f39///////Z2dj/QUtV/0xZZ/9NWmj/O0hU/0hPWP+Agoz/s7bE/+Xp+v/l6fv/8fX//7/C0P8ZGRr/AAAA/0hVY/9TYG//Sldk/0ZSXv9NWmj/UV5s/zlHVP+Chor///////7+/v//////////////////////////////////////+/z8//////+go6X/QU9d/zxHUv9zd4D/4+b2//3////9////9Pj///L2///s8P//7vL//+To+v+PkZz/NDpA/z5KVv9TYXD/UF1r/1Bda/9ATVz/cXV5/////////////v7+///////////////////////////////////////+/v7///////b29v9DTFT/j5Of//n8///t8f//3eHy/7u+zf+3usj/v8LR/9re8P/p7f7/6u7///r////V1+f/PT9E/zQ9Rv9BTlr/S1lo/1RcZP/39vX///////39/f////////////////////////////////////////////7+/v//////5OTk/29ze//2+f//5ur8/+/z///Lztz/aWyi/4eK0v9ucbT/kpSr//P3///m6v3/5Oj6//H1///j5vj/x8rZ/3+Ejv83RFH/kJSY///////6+/v//////////////////////////////////////////////////v7+///////c3Nv/rbC8//P4///m6vz/6e3//+nt+f+Mj7r/m5/+/36Bqf/h5fH/7PD//+js/v/p7f//5+v9/+ru///o7P7/+Pv//1hgbP92fIL///////39/f/////////////////////////////////////////////////8/Pz//////62trf+qrbv/9Pj//+Pn+P/l6fv/8/f//7S3zf9kZ5T/zdHe//L2///m6vz/5ur7/+fr/P/q7v//7PD//7C0wP/x9f//mZ6s/0VNVP/8+/v/////////////////////////////////////////////////////////////////nJ2j/6msuf/7////+v////H2///r7///5ur7/9PX5P/w9P//5+v9/+3x///6/v//9/v//+Hl9//x9f//v8LQ/9DU4//Dx9f/MTpC/9/f4P//////+vfz//////////////////////////////////////////////////39/P/IytL/oqWy/4WHkf9iY2v/y8/e/+Xp+//q7v//7vL//+fr/f/q7v//3eHy/5ueqv82Nzv/gYOM/93h8v9kaXL/paey/6isuP8sOEP/vsDB///////8+/v////////+/v/9+/n////////////58uz//fr3////////////+Pf2/3t+gf9wd4L/zdDf/0lKT/8AAAD/goWO//n9///k6Pn/6u7//+fr/f8XGBn/Dw8Q/5SWof/s8P//0tXl/zdCTf9YX2n/W2Js/zhGVP+anZ////////z8/P////////7+//nz7f///v3///////nz7f/8+ff//f3+//////+xsrP/Higx/4mRnv+pq7f/GRkb/1JUWv/W2er/7fH//+js/v/o7P7/7fH//4qMlv8nKCr/ERES/4aIkv/o6/z/TFZh/0RSYP9AS1b/QU9e/4SIjP///////Pz8//37+v////7////////////////////////////7+fj//////42Qk/8qN0P/fISR/7m6x/+nqrf//////+7y///n6/3/6e3//+nt///o7P7/+Pz//+zw//+OkJv/pKaz/8/T4/8/SlX/UV5t/1Bdav9ATVz/gYaK///////8/f3/+/fy//79/P////////////////////////////r59///////lpib/z9MWv9DT1r/d36J/7/C0f/JzNv/6u3//+ru///m6vz/6e3//+nt///o7P7/y87d/+nt///1+P//WGBr/0NQXf9QXWv/UV1r/z5MW/+Tl5v///////z8/P///////////////////////////////////////f39//////+8vL3/RlNf/0pXY/8/S1j/OkZR/11mcf+xtsT/7fH///P3///l6fv/7/P//7i7yf+bnan/19vq/42Snv87SVX/TVpp/0tYZv9OW2r/Qk9c/8TGyP///////P39///////////////////////////////////////+/v7///////79/P+Gjpb/OEVU/0FLVv9TYXD/Slhm/0dUYf9eZnD/tLjF//X5///r8P//5Oj6//T4///g5PT/SFFc/09da/9ibnr/VmJw/1Bda/9XYm3/9fX0///////+/v7////////////////////////////////////////////9/f3//////66ws/94go3/Tlhh/0RRXf9QXWv/Tltp/0dVY/82QUz/h4uW/9zf7//Aw9L//////6OntP86R1P/WWZz/4OMlf9XY3D/Slhm/3R6gf///////f3+//////////////////////////////////////////////////39/f//////zc3N/8zOz/+LlJ3/OERQ/3+Ikv9PW2n/Tltp/1Jgb/82Qk7/c3eB/2pwef+Eh5H/YGZv/0hWZP9OW2n/SFVk/09cav88SVf/wsPF///////8/P3////////////////////////////////////////////////////////////39/f/qamq/3J9if9EUWD/U19s/05baf9NWmj/TVln/1Febf9EUFz/P0VN/zpFT/88RlD/UF1r/0xZZ/9RXmv/QlBf/3R6gf///////v7+/////////////////////////////////////////////////////////////f39///////Y19b/jZCT/1pndf9JVmT/TVpo/01aaP9NWmj/TVln/1BdbP8+SVT/TVln/09cav9MWWf/UFxq/0tZaP9NWGP/6Ojo///////9/f3////////////9/f3//f39/////////////////////////////////////////////f39//////++vbz/f4SI/05cav9RXmz/T1tp/01aaP9NWmj/TVpo/09da/9NWmj/Tlto/1FebP9JV2b/QUxZ/8rLzf//////+/v7//7+/v///////////////////////////////////////////////////////////////////////v7+///////Ozcz/ZGpw/zhFU/9IVmX/T11r/1FebP9RXmz/UF1r/1BdbP9JV2b/Pkxb/1VeaP/Mzc7///////z9/f/////////////////29vb/0NDQ/7a2tv///////////////////////////////////////////////////////f39///////39vX/p6iq/15lbP9BTFf/PEhW/z1KWP89Slj/PktY/1xlb/+eoqf/8/Pz///////9/f3//f39/+3t7f/W1tb/zMzM/8HBwf+qqqr/vb29/////////////////////////////////////////////////////////////f39///////////////+/9fX1/+ur7H/mJud/5+hpP/Excb/+fj4/////////////Pz8///////8/Pz/19fX/9bW1v/y8vL//v7+/////////////////////////////////////////////////////////////////////////////v7+//z8/P///////////////////////////////////////Pz8//7+/v////////////7+/v/29vb//////////////////v7+//7+/v/////////////////////////////////////////////////////////////////////////////////9/f3//Pz8//v8/P/7/Pz//Pz8//7+/v/////////////////////////////////+/v7/////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='

ico = open('ShiHoIcon.ico', 'wb+')
ico.write(base64.b64decode(img)) 
ico.close()


root.iconbitmap('ShiHoIcon.ico')

os.remove('ShiHoIcon.ico')


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