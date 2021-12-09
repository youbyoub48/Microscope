from PySide2 import QtWidgets, QtGui, QtCore

from packages.API import Video

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.btn_cam = QtWidgets.QPushButton("Allumer la caméra")
        self.label_img = QtWidgets.QLabel()

    def create_layouts(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.btn_cam)
        
    def setup_connections(self):
        self.btn_cam.clicked.connect(self.film)
    
    def film(self):
        img_save = Video()
        if img_save == "save":
            img = QtGui.QPixmap("saved_img.jpg")
            self.label_img.setPixmap(img)
            self.label_img.setGeometry(QtCore.QRect(10, 40, img.width(), img.height()))
            self.main_layout.addWidget(self.label_img)
            self.resize(img.width()+20, img.height()+100)