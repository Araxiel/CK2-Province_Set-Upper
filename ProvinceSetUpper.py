from PyQt5 import QtWidgets
from _ui.MainWindow import MainWindow

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())