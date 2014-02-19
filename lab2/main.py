import sys
import csv

from PySide import QtGui
from pizza_ui import Ui_MainWindow


class CSV(object):
    """ CSV class for loading ingredients data.

    Can be extended to write new data, update data, etc
    """
    def __init__(self, filename):
        """ Initializer

        @param filename: valid path to a valid CSV file
        """
        self.filename = filename

    def load_ingredients(self):
        """ Load data about ingredients from CSV

        @rtype: dictionary
        @return: key/value of ingredients' names and their prices
        """
        data = {}
        with open(self.filename, 'rb') as csvfile:
            f = csv.reader(csvfile, delimiter=',')
            for row in f:
                data[row[0]] = int(row[1])
        return data


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
