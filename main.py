from calc import calc_passwd
from gui import Ui_MainWindow
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

version = 'v1.00'

def calc_Action(sn, obj):
    if sn != '':
        obj.pwEdit.setText(calc_passwd(sn))


if __name__ == '__main__':
    __qtApp = QApplication(sys.argv)
    __qtObj = QMainWindow()
    MainGui = Ui_MainWindow()
    MainGui.setupUi(__qtObj)
    __qtObj.setWindowTitle(__qtObj.windowTitle() +'_'+ version)
    __qtObj.setVisible(True)
    MainGui.pushButton.clicked.connect(lambda: calc_Action(MainGui.snEdit.text(), MainGui))
    sys.exit(__qtApp.exec())

