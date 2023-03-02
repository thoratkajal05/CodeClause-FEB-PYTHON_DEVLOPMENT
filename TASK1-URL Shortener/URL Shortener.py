import pyperclip
import pyshorteners 
from tkinter import *

root = Tk()
root.geometry("800x400")
root.title("URL Shortener")
root.configure(bg="black") 
url = StringVar()
url_addrerss = StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_addrerss.set(url_short)
    
def copyurl():
    url_short = url_addrerss.get()
    pyperclip.copy(url_short)

Label(root, text="My URL shortener", font="poppins").pack(pady=20)
Entry(root, textvariable=url).pack(pady=5) 
Button(root, text = "Generate Short URL", command = urlshortener).pack(pady=7)
Entry(root, textvariable=url_addrerss).pack(pady=5)
Button(root, text="Copy URL", command = copyurl).pack(pady=5)

root.mainloop()