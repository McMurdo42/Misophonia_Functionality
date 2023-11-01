from pygame import mixer
import time
import tkinter
from random import *


windowWidth = 700
windowHeight = 700


window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=windowWidth,height=windowHeight, bg="white")
#text = canvas.create_text(windowWidth/2,10,text=vel,fill="black",font=('Helvetica 15 bold'))

history = []


def dots(color,numdots,rectangle):
    colorList = ['Green','Magenta','Red','Blue','Orange','Cyan']
    dotlist = []
    size = 10
    total = 0
    for x in range(0,30):
        diffcolor = randint(0,5)
        while color == colorList[diffcolor]:
            diffcolor = randint(0,5)
        posx = randint(10,windowWidth-10)
        posy = randint(40,windowHeight-10)
        dotlist.append([canvas.create_oval(posx-size,posy-size,posx+size,posy+size,fill=colorList[diffcolor],outline="Black"),posx,posy])
        total += 1
    for x in range(0,numdots):
        posx = randint(10,windowWidth-10)
        posy = randint(40,windowHeight-10)
        dotlist.append([canvas.create_oval(posx-size,posy-size,posx+size,posy+size,fill=color,outline='Black'),posx,posy])
        total += 1
    canvas.itemconfig(rectangle, fill=color)
    
    canvas.update()
    return dotlist

def colorPick():
    colorList = ['Green','Magenta','Red','Blue','Orange','Cyan']
    return colorList[randint(0,5)]

def correctnum():
    return randint(10,19)

def key_press(event):
    global num, dotlist, history, color, rectangle
    key = event.char
    if key.isdigit():
        history.append([num, key, color, time.time()])
        File1.write(str(num))
        File1.write(',')
        File1.write(str(key))
        File1.write(',')
        File1.write(str(color))
        File1.write(',')
        File1.write(str(time.time()))
        File1.write(',')
        File1.write(sound)
        File1.write('\n')
        File1.truncate()
        for dot in range(0,30+num):
            canvas.delete(dotlist[dot][0])
        num = correctnum()
        color = colorPick()
        dotlist = dots(color, num, rectangle)


window.bind('<KeyPress>', key_press)


num = correctnum()
color = colorPick()
rectangle = canvas.create_rectangle(0,0,windowWidth,30,fill=color)
dotlist = dots(color, num, rectangle)


canvas.pack()


global File1
#filename = ("data_"+time.strftime("%Y%m%d_%H+%M+%S", time.localtime())+".txt")
filename = "data.txt"
File1 = open(filename,'w')


def soundPlayer():
    global sound
    soundList = ['Ahhh01.mp3','Ahhh02.mp3','Ahhh03.mp3','Ahhh04.mp3']
    sound = choice(soundList)
    mixer.init()
    mixer.music.load(sound)
    mixer.music.play()
    window.after(randint(5000,20000),soundPlayer)



soundPlayer()
window.mainloop()





'''
mixer.init()
mixer.music.load("SmallDogBark.mp3")
mixer.music.play()
'''