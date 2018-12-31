import tkinter as tk
import tkinter.filedialog as tkfiledialog
import tkinter.messagebox as tkmessagebox
import os
import moviepy.editor as mp
import time

DEBUG = True
debug = lambda s : print(s) if DEBUG else None


window = tk.Tk()
window.title("VComp")

text0 = tk.Label(window, text="The video you select will be compressed with file name \"compressed_originalfilename\"")
text0.pack()
PATH = ""

def dir_browser():
    global PATH
    b = tkfiledialog.askopenfile(title="Select a video to compress.")
    PATH = b.name

browser_button = tk.Button(window, text="Browse", command=dir_browser)
browser_button.pack()

text = tk.Label(window,text="Select Destination Video's height.")
text.pack()

def srvalcheck(*args):
    value = sr.get()
    nval = int(value/20) * 20
    sr.set(nval)
def brvalcheck(*args):
    value = br.get()
    nval = int(value/250) * 250
    br.set(nval)


sr = tk.Scale(window, from_=1, to=1080, orient=tk.HORIZONTAL, command=srvalcheck)
sr.set(480)
sr.pack(anchor=tk.CENTER)

text1 = tk.Label(window,text="Select Bitrate Level")
text1.pack()

br = tk.Scale(window, from_=1, to=3000, orient=tk.HORIZONTAL, command=brvalcheck)
br.set(500)
br.pack(anchor=tk.CENTER)


def read_compression_callback():
    global sr,br,read_compression,text,button_pressed,window, text1
    size = sr.get()
    sr.destroy()
    bit = br.get()
    br.destroy()
    text1.destroy()
    read_compression.destroy()
    text["text"] = "Status: Compressing..."
    text['padx'] = 10
    text['pady'] = 10
    text.pack()
    time.sleep(1)
    compress(size, bit, PATH)
    tkmessagebox.showinfo("Done","Done.")
    window.quit()

def get_new_filename(path):
    slash = path.rfind("/") + 1
    path0 = path[:slash]
    path1 = "compressed_"
    path2 = path[slash:]
    return path0+path1+path2

def compress(size, bit, f):
    SR = size
    BR = str(bit) + "k"
    video = mp.VideoFileClip(f)
    video_compressed = video.resize(height=SR)
    new_file = get_new_filename(f)
    video_compressed.write_videofile(new_file, bitrate=BR)


read_compression = tk.Button(window,text="Compress", command=read_compression_callback)
read_compression.pack()


def run():
    window.mainloop()
    window.destroy()

run()
