# pip install pyqt5
""" 
My Camera application

author: Mostafizur

 """

from operator import imod
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QIcon
import cv2

print("working....")

class Window(QWidget):
    """ Main App Window """

    def __init__(self):
        super().__init__()

        #vairables for app window
        self.window_width = 640
        self.window_height = 400

        # image vairables
        self.img_width = 640
        self.img_height = 400

        #setup the window
        self.setWindowTitle("My camera app")
        self.setGeometry(100, 200, self.window_width, self.window_height)
        self.setFixedSize(self.window_width, self.window_height)

        self.ui()

    def ui(self):
        """ Contains all ui things """
        # image label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0,0, self.img_width, self.img_height)

        self.show()

    def update(self):
        """ update frames """
        pass

    def save_img(self):
        """ Save the image from camera"""
        pass

    def record(self):
        """ Record the video from camera """
        pass


# run
app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec())



