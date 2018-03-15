from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon

class Window(QtGui.QPushButton):
    def __init__(self):
        QtGui.QPushButton.__init__(self, 'Choose a File')
        self.mediaObject = Phonon.MediaObject(self)
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.mediaObject, self.audioOutput)
        self.mediaObject.stateChanged.connect(self.handleStateChanged)
        self.clicked.connect(self.handleButton)

    def handleButton(self):
        if self.mediaObject.state() == Phonon.PlayingState:
            self.mediaObject.stop()
        else:
            path = QtGui.QFileDialog.getOpenFileName(self, self.text())
            if path:
                self.mediaObject.setCurrentSource(Phonon.MediaSource(path))
                self.mediaObject.play()

    def handleStateChanged(self, newstate, oldstate):
        if newstate == Phonon.PlayingState:
            self.setText('Stop')
        elif newstate == Phonon.StoppedState:
            self.setText('Choose a File')
        elif newstate == Phonon.ErrorState:
            source = self.mediaObject.currentSource().fileName()
            print 'ERROR: could not play:', source.toLocal8Bit().data()

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Phonon')
    win = Window()
    win.resize(200, 100)
    win.show()
    sys.exit(app.exec_())
    
    
    
    
    
    #This program is seperate from the one above. The first one is the working player, but without using Qt designer. The bottom one is my attempt to combine the two, but it is not fully working. 
    #When I click the play button, it changes from play to pause but then an error comes up and the computer files do not open in order to choose and play the .mp3 file. 
    
    
   
    
    
import sys
from PyQt4 import QtCore, QtGui, uic
import easygui
import random
    
form_class = uic.loadUiType("MediaPlayer.ui") [0]
    
    class MyWindowClass(QtGui.QMainWindow, form_class):
        def __init__(self, parent = None):
            QtGui.QMainWindow.__init__(self, parent)
            self.setupUi(self)
            self.pushButton.clicked.connect(self.button_clicked)
            
            def button_clicked(self, parent = None):
                if(self.Name.text () == "choose song from playlist"):
                    pygame.mixer.init()
                    pygame.mixer.music.load("musicfile.mp3")
                    pygame.mixer.music.play()
                    
        def button_clicked(self):
            if(self.pushButton.text() == "Play"):
                self.pushButton.setText("Pause")
                if self.mediaObject.state() == Phonon.PlayingSTate:
                    self.mediaObject.stop()
                else:
                    path = QtGui.QFileDialog.getOpenFileName(self, self.text())
             if path:
                self.mediaObject.setCurrentSource(Phonon.MediaSource(path))
                self.mediaObject.play()
            else:
                self.pushButton.setText("Play")
                print("Testing...")
                print("It looks like it's working")
       
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()







#pygame mix
import sys
from PyQt4 import QtCore, QtGui, uic
import easygui
import pygame
import time
import random

form_class = uic.loadUiType("radio.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.Play.clicked.connect(self.button_clicked)
        self.Song1.clicked.connect(self.button_clicked3)
        self.Skip.clicked.connect(self.button_clicked6)
        self.Shuffle.clicked.connect(self.button_clicked7)
    def button_clicked(self, parent = None):
        if(self.Name.text () == "Choose Song from Playlist"):
            self.Name.setText("Song1")
            pygame.mixer.init()
            pygame.mixer.music.load('Sistar - I Like That.mp3')
            pygame.mixer.music.play()
        elif(self.Name.text () == "Song2"):
            pygame.mixer.init()
            pygame.mixer.music.load('Michael Jackson - Smooth Criminal Lyrics.mp3')
            pygame.mixer.music.play()
        elif(self.Name.text () == "Song3"):
            pygame.mixer.init()
            pygame.mixer.music.load("SUPER JUNIOR 슈퍼주니어 'Black Suit' MV.mp3")
            pygame.mixer.music.play()
    def button_clicked2(self, parent = None):
        pygame.mixer.music.pause()
    def button_clicked3(self):
        self.Name.setText("Song1")
    def button_clicked4(self):
        self.Name.setText("Song2")
    def button_clicked5(self):
        self.Name.setText("Song3")
    def button_clicked6(self, parent = None):
        if(self.Name.text () == "Song1"):
            self.Name.setText("Song2")
            pygame.mixer.music.load('Michael Jackson - Smooth Criminal Lyrics.mp3')
            pygame.mixer.music.play()
        elif(self.Name.text () == "Song2"):
            self.Name.setText("Song3")
            pygame.mixer.music.load("SUPER JUNIOR 슈퍼주니어 'Black Suit' MV.mp3")
            pygame.mixer.music.play()
            
    def button_clicked7(self):
        songshuffle1 = ['Song2', 'Song3']
        songshuffle2 = ['Song1', 'Song3']
        songshuffle3 = ['Song1', 'Song2']
        if(self.Name.text () == "Song1"):
            self.Name.setText(random.choice(songshuffle1))
            if(self.Name.text () == "Song2"):
                pygame.mixer.music.load('Michael Jackson - Smooth Criminal Lyrics.mp3')
                pygame.mixer.music.play()
            elif(self.Name.text () == "Song3"):
                pygame.mixer.music.load("SUPER JUNIOR 슈퍼주니어 'Black Suit' MV.mp3")
                pygame.mixer.music.play()
        elif(self.Name.text () == "Song2"):
            self.Name.setText(random.choice(songshuffle2))
            if(self.Name.text () == "Song1"):
                pygame.mixer.music.load('Sistar - I Like That.mp3')
                pygame.mixer.music.play()
            elif(self.Name.text () == "Song3"):
                pygame.mixer.music.load("SUPER JUNIOR 슈퍼주니어 'Black Suit' MV.mp3")
                pygame.mixer.music.play()
        elif(self.Name.text () == "Song3"):
            self.Name.setText(random.choice(songshuffle3))
            if(self.Name.text () == "Song1"):
                pygame.mixer.music.load('Sistar - I Like That.mp3')
                pygame.mixer.music.play()
            elif(self.Name.text () == "Song2"):
                pygame.mixer.music.load('Michael Jackson - Smooth Criminal Lyrics.mp3')
                pygame.mixer.music.play()
pygame.quit()
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
        
