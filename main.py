import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Random Circles')

        self.btn = QPushButton('Draw Circle', self)
        self.btn.clicked.connect(self.drawCircle)
        self.btn.move(100, 150)

    def drawCircle(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor("yellow"))
        diameter = random.randint(10, 100)
        qp.drawEllipse(50, 50, diameter, diameter)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())