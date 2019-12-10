from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication

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

    def coffee_init(self):
        db = DbInit()
        db.service()

    def Backup(self):
        br = BackupRestore()
        br.data_backup(table_name='product')
        br.data_backup(table_name='sale')

    def Restore(self):
        br = BackupRestore()
        br.data_restore(table_name='product')
        br.data_restore(table_name='sale')

