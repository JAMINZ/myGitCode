# -*- coding: utf-8 -*-
from tkinter import *      # ���� Tkinter ��
import time,datetime,winsound,threading
root = Tk() 
lbl = Label(root,text ="hello,world",width = 30,height = 2)
def tick():
  global timer
  timer = threading.Timer(1.0,tick,"")
  currenttime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
  lbl.config(text = currenttime)  
  currenttime1 = datetime.datetime.now()
  if currenttime1.minute == 0 and currenttime1.second == 0 and currenttime1.hour > 5 and currenttime1.hour < 23:
    winsound.Beep(1000,5000)
    #����600��ʾ������С��1000��ʾ����ʱ����1000Ϊ1��
  lbl.pack() # ��С�������õ���������
  timer.start()
if __name__ == "__main__":
  timer = threading.Timer(1.0,tick,"")
  timer.start()

root.mainloop()
