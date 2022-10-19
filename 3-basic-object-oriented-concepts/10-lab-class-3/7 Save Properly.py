# pip install pyqt5
""" 
My Camera application

author: Mostafizur

 """

from operator import imod
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import QTimer
import cv2
import datetime

print("Opening Camera please wait....")

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

        # load icon
        self.camera_icon = QIcon(cam_icon_path)
        self.rec_icon = QIcon(rec_icon_path)

        #setup the window
        self.setWindowTitle("My camera app")
        self.setGeometry(100, 200, self.window_width, self.window_height)
        self.setFixedSize(self.window_width, self.window_height)

        # setup Timer
        self.Timer = QTimer()
        self.Timer.timeout.connect(self.update)

        self.ui()

    def ui(self):
        """ Contains all ui things """
        # layout
        grid = QGridLayout()
        self.setLayout(grid)

        # image label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0,0, self.img_width, self.img_height)

        # capture button
        self.capture_btn = QPushButton(self)
        self.capture_btn.setIcon(self.camera_icon)
        self.capture_btn.setStyleSheet("border-radius: 30; border : 2px solid black; border-width: 3px")
        self.capture_btn.setFixedSize(60, 60)
        self.capture_btn.clicked.connect(self.save_img)

        # record button
        self.rec_btn = QPushButton(self)
        self.rec_btn.setIcon(self.rec_icon)
        self.rec_btn.setStyleSheet("border-radius: 30; border : 2px solid black; border-width: 3px")
        self.rec_btn.setFixedSize(60, 60)
        self.rec_btn.clicked.connect(self.record)

        if not self.Timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.Timer.start(20)
        
        # add things to the layout
        grid.addWidget(self.capture_btn, 0, 0)
        grid.addWidget(self.image_label, 0, 1, 2, 3)
        grid.addWidget(self.rec_btn, 1, 0)

        self.show()

    def update(self):
        """ update frames """
        _, self.frame = self.cap.read()

        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB) 
        height, width, channel = frame.shape
        step = channel * width

        q_frame = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(q_frame))

    def save_img(self):
        """ Save the image from camera"""
        print("Saving Image")
        self.get_time()
        cv2.imwrite(f"{self.dt}.jpg", self.frame)
        print("Image saved successfully!")

    def record(self):
        """ Record the video from camera """
        print("Recording")

    def get_time(self):
        now = datetime.datetime.now()
        self.dt = now.strftime("%m-%d-%y, %H-%M-%S")
        print(self.dt)

# run

cam_icon_path = 'assets/camera.png'
rec_icon_path = 'assets/video-camera.png'

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec())



