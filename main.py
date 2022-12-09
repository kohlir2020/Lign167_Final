# main file runner

import sys
import os
from PyQt5.QtWidgets import * #QMainWindow, QApplication, QWidget, QPushButton, QAction, QPlainTextEdit, QMessageBox
from PyQt5 import QtCore
from PyQt5.QtGui import * 
from PyQt5.QtCore import pyqtSlot
import openai
from model import *

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Poem Title Generator'
        self.left = 10
        self.top = 10
        self.right = 10
        self.bottom = 10
        self.width = 600
        self.height = 600

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.setStyleSheet('background-color: #f08686; \
                            selection-background-color: #3d8ec9; \
                            selection-color: black; \
                            background-clip: border; \
                            outline: 3')
    
        # Create label for textbox
        self.label = QLabel('Enter your poem in the textbox below:', self)
        self.label.move(25, 20)
        self.label.resize(250, 20)
        #self.label.setStyleSheet('border: 1px solid #3A3939; color: black; margin: 1px;')

        # Create label for instructions
        self.label1 = QLabel('This is a Poem Title Generator. It is an application of a Deep Learning model. This application is a pre-trained BART model fine-tuned on a corpus of Poem-Title pairs from the PoetryFoundation.\nPlease write a poem in the textbox to the left. Click the button below to generate an appropriate title for your poem.', self)
        self.label1.setWordWrap(True)
        self.label1.resize(250, 200)
        self.label1.move(300, 50)
        self.label1.setStyleSheet('border: 1px solid #3A3939; color: black; margin: 1px;')

        # Create textbox for poem input
        self.textbox = QPlainTextEdit(self)
        self.textbox.move(20, 50)
        self.textbox.resize(250,300)
        
        # Create a button in the window
        self.button = QPushButton('Generate Title', self)
        self.button.move(300,300)
        self.button.resize(150, 50)
        #self.button.setStyleSheet('border: 1px solid #3A3939; margin: 1px;')
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        
        # shows the window to the APP
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.toPlainText()
        title = getTitle_1(textboxValue)
        QMessageBox.question(self, 'Text goes here', "Title: " + title, QMessageBox.Ok, QMessageBox.Ok)
        #self.output = QLabel("Title: " + title, self)
        #self.output.move(300, 450)
        #self.output.setStyleSheet('background-color: #3d8ec9; padding: 2px; border-style: solid; border: 1px solid #3A3939; border-radius: 2px; color: black;')

if __name__ == '__main__':

    loadTransform() # this loads in our fine-tuned model
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


