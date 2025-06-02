from PyQt6 import uic
from PyQt6.QtWidgets import (QWidget, QLabel, QApplication, QMessageBox)
from PyQt6.QtGui import (QIcon, QPixmap)
from addtionwindow import AddWindow
from displaywindow import DisplayWindow
from searchwindow import SearchWidow
from data import Db
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.db=Db()
        IMG_PATH= '../../images/pexels-moose-photos-170195-1037993.jpg'
        UI_PATH= './UI_files/gym.ui'
        ICON_PATH= '../../images/pexels-moose-photos-170195-1037993.jpg'
        uic.loadUi(UI_PATH,self)
        self.setWindowIcon(QIcon(ICON_PATH))
        img=QPixmap(IMG_PATH).scaled(self.width(),self.height())
        img_label=QLabel(self)
        img_label.setPixmap(img)
        img_label.lower()
        self.connect_buttons()
        self.show()
    def connect_buttons(self):
        self.label.setStyleSheet('color:black;')
        self.btnadd.clicked.connect(self.open_add_window)
        self.btndisplay.clicked.connect(self.open_display_window)
        self.btnsearch.clicked.connect(self.open_search_window)
        self.btnexit.clicked.connect(self.exitbtn)
    def open_display_window(self):
        self.display= DisplayWindow()
        self.display.show()
    def open_add_window(self):
        self.addwindow=AddWindow()
        self.addwindow.show()
    def open_search_window(self):
        self.search_window=SearchWidow()
        self.search_window.show()
    def closeEvent(self,event):
        "يتم استدعائها تلقائيا"
        replay= QMessageBox.question(self,'Confirm','Are you sure you want to exit?')
        if replay == QMessageBox.StandardButton.Yes :
            event.accept()
            self.db.close()
        else:
            event.ignore()
    def exitbtn(self):
        self.close()  # هتشغل دالةcloseEvent  

app=QApplication([])
win=MainWin()
app.exec()