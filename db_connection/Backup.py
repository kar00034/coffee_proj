
from mysql.connector import Error

from db_connection.explicitly_connection_pool import ExplicitlyConnectionPool


class BackupRestore:

    OPTION = """
        CHARACTER SET 'UTF8'
        FIELDS TERMINATED by ','
        LINES TERMINATED by '\r\n';
        """

    def __init__(self, source_dir='/home/jh/PycharmProjects/python_mysql_study/restore_backup/data/', data_dir='/home/jh/PycharmProjects/python_mysql_study/restore_backup/data/'):
        self.source_dir = source_dir
        self.data_dir = data_dir

    def data_backup(self, table_name):
        filename = table_name+'.txt'
        try:
            conn = ExplicitlyConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            cursor.execute("use coffee")
            source_path = self.source_dir + filename

            backup_sql = "SELECT * FROM {} INTO OUTFILE '{}' {}".format(table_name, source_path, BackupRestore.OPTION)
            cursor.execute(backup_sql)

            print(table_name, "backup complete!")
        except Error as err:
            print(err)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def data_restore(self, table_name):
        conn = ExplicitlyConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute("use coffee")
        filename = table_name + '.txt'
        try:
            source_path = self.source_dir + filename

            restore_sql = "LOAD DATA INFILE '{}' into table {} {}".format(source_path, table_name, BackupRestore.OPTION)
            cursor.execute(restore_sql)
            conn.commit()
            print(table_name, "restore complete!")
        except Error as err:
            print(err)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
