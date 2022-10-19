# pip install pyqt5
""" 
My Camera application

author: Mostafizur

 """

# from operator import imod
import sys
from turtle import width
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

        # other Variables
        self.dt = '0-0-0'
        self.record_flag = False

        # load icon
        self.camera_icon = QIcon(cam_icon_path)
        self.rec_icon = QIcon(rec_icon_path)
        self.stop_icon = QIcon(stop_icon_path)

        # to save the video 
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')

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
        copy_frame = self.frame
        if self.record_flag == True:
            print("Recording....")
            self.out.write(copy_frame)       
            self.rec_btn.setIcon(self.stop_icon)
            self.frame = cv2.circle(self.frame, (20,70), 5, (0,0,255), 10)

        else:
            self.rec_btn.setIcon(self.rec_icon)

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
        # print("Recording...")
        print(self.record_flag)

        if self.record_flag == True:
            self.record_flag = False
            print("Stopping recording")
        
        else:
            self.record_flag = True
            print("Starting to record")
            self.get_time()

            self.out = cv2.VideoWriter(f"{self.dt}.avi", self.fourcc, 20.0, (640,480))

    def get_time(self):
        now = datetime.datetime.now()
        self.dt = now.strftime("%m-%d-%y, %H-%M-%S")
        print(self.dt)

# run
if __name__ == '__main__':
    cam_icon_path = 'assets/camera.png'
    rec_icon_path = 'assets/video-camera.png'
    stop_icon_path = 'assets/stop-button.png'

    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec())


