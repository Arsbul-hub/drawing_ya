import random
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw_btn.clicked.connect(self.repaint)

    def paintEvent(self, event):
        qp = QPainter()

        qp.begin(self)
        qp.setPen(QPen(Qt.yellow))
        qp.setBrush(Qt.yellow)
        for i in range(30):
            radius = random.randint(10, 70)
            qp.drawEllipse(random.randint(0, self.width()),
                           random.randint(self.draw_btn.y() + self.draw_btn.height(), self.height()), radius, radius)

        qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
