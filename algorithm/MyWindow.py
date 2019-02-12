from PyQt5.QtGui import *
from PyQt5.Qt import QMainWindow, QFormLayout
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtGui

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_BrowserReload)))
window.setWindowTitle("my job")


widget = QWidget()
window.setCentralWidget(widget)
widget.setBaseSize(500, 400)
widget.setGeometry(300, 300, 300, 150)
hbox = QHBoxLayout()
widget.setLayout(hbox)
close = QPushButton("&Close")
close.clicked.connect(window.close)

# q = QFormLayout()
# q.addRow(QLabel("This is a label"), QPushButton("nothing"))
# q.addRow(QLabel("label 2"), close)
widget.show()

p = QPainter()
p.setPen(QColor(55, 34, 3))
p.begin(widget)
p.drawLine(5,5,100,500)
# p.end()




# widget.setLayout(q)

window.show()

app.exec_()


