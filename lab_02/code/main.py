import sys

from PyQt6.QtWidgets import *

from ui.app import LabWinodw

app = QApplication(sys.argv)
window = LabWinodw()
window.show()

app.exec()


