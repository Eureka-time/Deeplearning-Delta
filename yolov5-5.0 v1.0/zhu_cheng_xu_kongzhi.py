from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import zhu_cheng_xu
import shuju
from time import *
class kongzhi(QMainWindow,zhu_cheng_xu.Ui_Form):
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        zhu_cheng_xu.Ui_Form.__init__(self)
        self.setupUi(self)
        self.L_x.setText('1')
        sleep(3)
        shuju.kaishi()
        # print(x_min,y_min,xyz)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    checkboxDemo = kongzhi()
    checkboxDemo.show()
    sys.exit(app.exec_())
        
