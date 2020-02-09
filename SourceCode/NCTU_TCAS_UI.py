#!/usr/bin/python
# -*- coding: UTF-8 -*-
from NCTU_TCAS_crawling import *
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import os
li=[]

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("NCTU TCAS")
        self.geometry('900x600')
        self.resizable(width=False, height=False)
        self.iconbitmap('icon32.ico')
        
        #background
        img = ImageTk.PhotoImage(Image.open("bg1.png").resize((900, 600), Image.ANTIALIAS))
        panel = tk.Label(self, image=img)
        panel.image=img
        panel.place(relx=.5,rely=.5,anchor='c')

        def enter(event):
            page2()
        #page containings  
        entry = tk.Entry(self,width=20,font=('微軟正黑體', 16))
        entry.place(relx=.5,rely=.5,anchor='c') 
        entry.bind('<Return>',enter)
        
        s = tk.ttk.Style()
        s.configure('my.TButton', font=('標楷體', 18))
  
        button = tk.ttk.Button(self, text="開始搜尋",style='my.TButton', command=lambda: page2())
        button.place(relx=.5,rely=.58,anchor='c')
       
        
        label = tk.Label(self, text="本系統提供有關交通大學相關網站中的教授和課程評價與心得之整合查詢", font=("微軟正黑體", 12),bg='#FFFEFA')
        label.place(relx=.5,rely=.95,anchor='c')#顯示位置
        
        label2 = tk.Label(self, text="Source From:  https://plus.nctu.edu.tw/  &  https://www.ptt.cc/bbs/NCTU-Teacher/index727.html", font=("微軟正黑體", 9),bg='#FFFEFA')
        label2.place(relx=.5,rely=.98,anchor='c')#顯示位置
  
        button1 = tk.ttk.Button(self, text="離開系統",style='my.TButton', command=lambda: self.destroy() )
        button1.place(relx=.917,rely=.965,anchor='c')
        
        #waring label
        label3 = tk.Label(self, text='', font=("標楷體",18),bg='#FFFEFA',fg='red')
        label3.place(relx=.5,rely=.9,anchor='c')#顯示位置

        def enter2(event):
            search()
            
        def page2():
            global lb,text,txt,n
            n=getTitle(entry.get())           
            
            if entry.get() == '':
                label3.config(text='請輸入搜尋詞！！！')                
            elif len(n[0])==0:
                label3.config(text='查無結果！！！')
                
            else:
                txt=getnText(entry.get())
                entry.place(relx=.59,rely=.14,anchor='c')
                entry.bind('<Return>',enter2)
                button.place(relx=.81,rely=.14,anchor='c')
                button.config(command=lambda: search())
                
                #change background
                img2 = ImageTk.PhotoImage(Image.open("bg2.png").resize((900, 600), Image.ANTIALIAS))
                panel.config(image=img2)
                panel.image=img2
                
                #Listbox for title
                var = tk.StringVar()
                lb = tk.Listbox(self, height=4, selectmode=tk.BROWSE, listvariable = var,font=("微軟正黑體", 12))
                lb.bind('<ButtonRelease-1>', print_item)
                for item in n[0]:
                    lb.insert(tk.END, item)           
                lb.pack(ipadx=230,pady=118,anchor='c')
		
                #textbox for particals
                text = tk.Text(self,height=15,width=85,font=("微軟正黑體", 12),state=tk.DISABLED)
                text.place(relx=.5,rely=.63,anchor='c')

                label3.config(text='')
                
        def search():
            global txt,n
            n=getTitle(entry.get())
	    
            if entry.get() == '':
                label3.config(text='請輸入搜尋詞！！！')                
            elif len(n[0])==0:
                label3.config(text='查無結果！！！')
            else:
                label3.config(text='')
                lb.delete(0,'end')
                txt=getnText(entry.get())
                for item in n[0]:
                    lb.insert(tk.END, item)          
            
        def print_item(event):
            global txt            
            value = lb.curselection()
            text.config(state=tk.NORMAL)
            text.delete(1.0,'end')
            if value[0]<n[1]:
                text.insert(1.0,txt[value[0]])
            else:
                text.insert(1.0,getpText(n[2],value[0]-n[1]))
            text.config(state=tk.DISABLED)
                        

if __name__=='__main__':
    app = Application()
    app.mainloop()
