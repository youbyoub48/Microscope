from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import qimage2ndarray

import cv2
import sys

class MainApp(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.video_size = QSize(320, 240)
        self.setup_ui()
        self.setup_camera()

    def setup_ui(self):
        """Initialize widgets.
        """
        self.image_label = QLabel()
        self.image_label.setFixedSize(self.video_size)

        self.btn_save = QPushButton("Screenshot")
        self.btn_save.clicked.connect(self.save)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.image_label)
        self.main_layout.addWidget(self.btn_save)

        QShortcut(QKeySequence("s"), self.image_label, self.save)

        self.setLayout(self.main_layout)

    def setup_camera(self):
        """Initialize camera.
        """
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)

    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        image = qimage2ndarray.array2qimage(frame)  #SOLUTION FOR MEMORY LEAK
        self.image_label.setPixmap(QPixmap.fromImage(image))
        self.frame = frame
    
    def save(self):
        cv2.imwrite(filename='saved_img.jpg', img=self.frame)
        cv2.imread('saved_img.jpg')
        cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
        print("save")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainApp()
    win.show()
    sys.exit(app.exec_())