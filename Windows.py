import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QHBoxLayout, QSystemTrayIcon, QLineEdit)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication, Qt
import subprocess
import SystemTrayIcon


class Windows(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')
        self.tray_icon = SystemTrayIcon.SystemTrayIcon(QIcon('idea.png'), self)
        self.tray_icon.show()
        # self.setStylesheet("border-radius: 10px")
        # self.autoFillBackground(True)
        
        btn = QPushButton('Кнопка', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(100, 10)
        btn.clicked.connect(Windows.notif)
        
        exit = QPushButton('Выход', self)
        exit.resize(btn.sizeHint())
        exit.move(10, 10)
        exit.clicked.connect(QCoreApplication.instance().quit)

        textSearch = QLineEdit(self)
        textSearch.move(200, 10)
        textSearch.resize(470, 26)
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn)
        hbox.addWidget(exit)
        hbox.addWidget(textSearch)
        

        self.setGeometry(1500, 400, 700, 47)
        self.setWindowTitle('Tooltips')
        self.setWindowFlags(Qt.FramelessWindowHint)


        # self.tray_icon.showMessage(
        #         "Tray Program",
        #         "Application was minimized to Tray",
        #         QSystemTrayIcon.Information,
        #         2000
        #     )
        self.show()

    def notif(self, text):
        subprocess.Popen(['notify-send', text])

        # self.tray_icon.showMessage(
        #         "Tray Program",
        #         "Application was minimized to Tray",
        #         QSystemTrayIcon.Information,
        #         2000
        #     )