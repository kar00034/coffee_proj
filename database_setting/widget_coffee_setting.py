from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox

from db_connection.Backup import BackupRestore
from db_connection.coffee_init_service import DbInit


class Coffee(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("database_setting/coffee.ui")
        self.ui.show()

        btn_init = self.ui.btn_init.clicked.connect(self.coffee_init)
        btn_backup = self.ui.btn_backup.clicked.connect(self.Backup)
        btn_restore = self.ui.btn_restore.clicked.connect(self.Restore)

    def msgbox1(self):
        QMessageBox.information(self, "Success", "초기화 성공")

    def msgbox2(self):
        QMessageBox.information(self, "Failed", "초기화 실패")

    def msgbox3(self):
        QMessageBox.information(self, "Success", "백업 성공")

    def msgbox4(self):
        QMessageBox.information(self, "Success", "복구 성공")

    def coffee_init(self):
        db = DbInit()
        # db.service()
        if db.service() == 0:
            self.msgbox1()
        else:
            self.msgbox2()

    def Backup(self):
        br = BackupRestore()
        br.data_backup(table_name='product')
        br.data_backup(table_name='sale')
        self.msgbox3()


    def Restore(self):
        br = BackupRestore()
        br.data_restore(table_name='product')
        br.data_restore(table_name='sale')
        self.msgbox4()

