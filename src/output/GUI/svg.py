import sys
from PyQt5 import QtGui, QtSvg
from PyQt5.QtWidgets import QApplication
# from IPython.display import SVG, display

app = QApplication(sys.argv)

svgWidget = QtSvg.QSvgWidget('/circle.svg');
#svgWidget.setGeometry(50,50,759,668)
svgWidget.show()

sys.exit(app.exec_())