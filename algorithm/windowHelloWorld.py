import sys
from PyQt5.QtGui import *
from PyQt5.Qt import QWidget, QLabel, QApplication
from PyQt5 import Qt

def window():
   app = QApplication(sys.argv)
   w = QWidget()
#    b = QLabel(w)
#    b.setText("Hello World!")
   w.setGeometry(100,100,200,50)
#    b.move(50,20)
   w.setWindowTitle("test")
   w.show()
   
   
   painter = QPainter()
   painter.setRenderHint(QPainter.Antialiasing)
   painter.setBackground(QColor(0, 200, 0))
   painter.setBrush(QColor(0, 0, 200))
#    painter.setPen(QPen(QColor(0, 0, 200), 2, Qt.SolidLine))
   painter.drawEllipse(40, 40, 40, 40)
#    painter.setBrush(Qt.NoBrush)
        
   sys.exit(app.exec_())
    
if __name__ == '__main__':
   window()