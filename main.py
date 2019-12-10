from PyQt5.QtWidgets import QApplication
from database_setting.widget_coffee_setting import Coffee

if __name__ == "__main__":
    app = QApplication([])
    w = Coffee()
    app.exec_()

