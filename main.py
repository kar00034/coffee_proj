from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication


class Coffee(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("database_setting/coffee.ui")
        self.ui.show()


if __name__ == "__main__":
    app = QApplication([])
    w = Coffee()
    app.exec_()
