import sys

from PySide import QtGui
from pizza_ui import Ui_MainWindow


class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    pizza_app = ControlMainWindow()
    pizza_app.show()
    sys.exit(app.exec_())
