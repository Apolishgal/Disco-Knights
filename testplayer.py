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

#playing music on pygame
#pygame.init()
#pygame.mixer.init()
#screen = pygame.display.set_mode([640,480])
#pygame.time.delay(1000)
#pygame.mixer.music.load('Sistar - I Like That.mp3')
#pygame.mixer.music.play()
form_class = uic.loadUiType("radio.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        if(self.pushButton.text () == "Play"):
            self.pushButton.setText("Pause") 
        else:
            self.pushButton.setText("Play")
        print("Testing...")
        print("It looks like its working")

        pygame.mixer.init()
        pygame.display.init()
        playlist = list()
        playlist.append ( 'Sistar - I Like That.mp3' )
        playlist.append ( 'Michael Jackson - Smooth Criminal Lyrics.mp3' )
        playlist.append ( "SUPER JUNIOR 슈퍼주니어 'Black Suit' MV.mp3" )
        pygame.mixer.music.load ( playlist.pop() )
        pygame.mixer.music.play()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
        
pygame.quit()
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
        
