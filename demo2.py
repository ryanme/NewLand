# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/9/9 14:21
from tkinter import *
import time

num = 0

tk = Tk()

main_frame = Frame(tk)
text_frame = Frame(main_frame)
ip_frame = Frame(main_frame)


text = Text(text_frame, width=30, height=25)
text.pack()

while num < 7:
    num += 1
    text.update()
    # canvas.itemconfig(itext, text=str(num))
    # canvas.insert(itext, 12, '')
    # tk.update()
    # print('num=%d' % num)
    # tk.after(1000)

main_frame.pack()
ip_frame.pack(side='top', pady='5')
text_frame.pack()
tk.mainloop()


# canvas = Canvas(tk, width=500, height=500)
# canvas.pack()
# itext = canvas.create_text(30, 30, text=str(num))
# while num < 7:
#     num += 1
#     canvas.itemconfig(itext, text=str(num))
#     canvas.insert(itext, 12, '')
#     tk.update()
#     print('num=%d' % num)
#     tk.after(1000)