'''
Created on Jan 11, 2018

@author: Antoine Ho

This program plays mp3 files.
GUI: tkinter
mp3 player library: pygame
Lists mp3 files in the music folder
'''

from tkinter import *
from pygame import mixer
import os

class MainWindow:
    
    '''
    This is the Window that shows up
    '''
    
    def __init__(self, master):
        
        master.title('mp3 Player')
        #-------- Frames in master --------        
        #** frame that holds the music list **
        musicFrame=Frame(master)
        musicFrame.pack(fill=BOTH, expand=1)
        
        #** frame that holds the volumebar **
        statusFrame=Frame(master, height=23)
        statusFrame.pack(fill=BOTH)
        
        #** frame that holds the buttons **
        buttonFrame=Frame(master)
        buttonFrame.pack(side=BOTTOM, fill=BOTH)

        #-------- Songs --------
        #** scrollbar **
        scrollMusic = Scrollbar(musicFrame)
        scrollMusic.pack(side=RIGHT, fill=Y)
        
        #** ListBox **
        self.songsList = [s for s in os.listdir(".\\music") if s.endswith(".mp3")]
        self.songs = Listbox(musicFrame, yscrollcommand=scrollMusic.set, width=75, height=15)
        
        #inserts the songs in the self.songs Listbox
        x = 0
        for i in self.songsList:
            self.songs.insert(x, i)
            x += 1
            
        self.songs.pack(fill=BOTH, expand=1)
        self.songs.bind("<Double-Button-1>", self.playSong, self.volume)
        
        scrollMusic.config(command=self.songs.yview)

        #-------- Music Status --------
        volumeBar = Scale(statusFrame, orient=HORIZONTAL, from_=0.0, to=1.0, resolution=0.01, 
                          command=self.volume)
        volumeBar.pack(side=RIGHT)
        
        #-------- Buttons --------
        #** Unpause Button **
        self.playButton = Button(buttonFrame, text="Play", command=self.unpauseMusic)
        self.playButton.pack(fill=BOTH, side=BOTTOM)
        
        #** Pause Button **
        self.stopButton = Button(buttonFrame, text="Pause", command=self.pauseMusic)
        self.stopButton.pack(fill=BOTH, side=BOTTOM)

    
    def playSong(self, event):
            widget = event.widget
            selection = widget.curselection()
            #value is the music file name
            value = widget.get(selection[0])
            mixer.init()
            loud = mixer.music.get_volume()
            
            #So that the music doesn't start playing really loud
            if loud == 0.9921875:
                mixer.music.set_volume(0)
            
            #loads and plays the music in the dir
            mixer.music.load('.\\music\\' + value)
            mixer.music.play()
       
    def pauseMusic(self):
        mixer.music.pause()
        
    def unpauseMusic(self):
        mixer.music.unpause()

    def volume(self, val):        
        mixer.init()
        mixer.music.set_volume(float(val))
        
        
root = Tk()

mainBoy = MainWindow(root)

root.mainloop()



















