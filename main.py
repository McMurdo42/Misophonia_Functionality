from pygame import mixer
import time
import tkinter
from random import *


windowWidth = 300
windowHeight = 300


window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=windowWidth,height=windowHeight, bg="white")
#text = canvas.create_text(windowWidth/2,10,text=vel,fill="black",font=('Helvetica 15 bold'))


inputtxt = tkinter.Text(window,height=1,width=3)

def dots(color,numdots):
    colorList = ['Green','Yellow','Red','Blue','Orange','Black']
    dotlist = []
    size = 3
    for x in range(0,numdots):
        posx = randint(10,windowWidth-10)
        posy = randint(10,windowHeight-10)
        dotlist.append(canvas.create_oval(posx-size,posy-size,posx+size,posy+size,fill=color,outline=color))
    for x in range(0,30):
        diffcolor = randint(0,5)
        while color == colorList[diffcolor]:
            diffcolor = randint(0,5)
        posx = randint(10,windowWidth-10)
        posy = randint(10,windowHeight-10)
        dotlist.append(canvas.create_oval(posx-size,posy-size,posx+size,posy+size,fill=colorList[diffcolor],outline=colorList[diffcolor]))
    return dotlist

def colorPick():
    colorList = ['Green','Yellow','Red','Blue','Orange','Black']
    return colorList[randint(0,5)]

def correctnum():
    return randint(10,20)

def submit(event):



canvas.pack()









mixer.init()
mixer.music.load("SmallDogBark.mp3")
mixer.music.play()