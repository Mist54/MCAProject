from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget

import main
from Designer.Test import Ui_Form


class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.main = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.openMain)

    def openMain(self):
        self.close()
        self.main=main.MainWindow()
        self.main.show()


if __name__ == '__main__':
    app = QApplication([])
    form = Ui_Form()
    widget = QWidget()
    form.setupUi(widget)
    widget.show()
    app.exec()
