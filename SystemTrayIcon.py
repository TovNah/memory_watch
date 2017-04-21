import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QSystemTrayIcon

class SystemTrayIcon(QSystemTrayIcon):
    parent =None

    def __init__(self, icon, parent=None):
        SystemTrayIcon.parent = parent
        super(SystemTrayIcon, self).__init__(icon, parent)
        menu = QMenu(parent)
        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect(parent.close)
        self.setContextMenu(menu)
        self.activated.connect(SystemTrayIcon.eActivated)
        # self.parent.show

    def eActivated(self):
        SystemTrayIcon.parent.show()
        print('3425')

