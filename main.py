import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.db")
        self.select_data()
        self.tableWidget.verticalHeader().setVisible(False)

    def select_data(self):
        q = self.connection.cursor().execute("SELECT * FROM data")
        res = q.fetchall()
        self.tableWidget.setColumnCount(7)
        names = list(map(lambda x: x[0], q.description))
        self.tableWidget.setHorizontalHeaderLabels(names)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
