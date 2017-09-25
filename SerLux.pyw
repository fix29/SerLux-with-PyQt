import serial.tools.list_ports
import warnings
import sip
import serial
import sys, time, os
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QAction, QApplication, QFrame,QDialog, QIcon, QMainWindow, QMenu, QSystemTrayIcon
from newstyle import Ui_Dialog
from contextlib import contextmanager

class Workthread(QtCore.QThread):
        def __init__(self, parent = None):
                QtCore.QThread.__init__(self,parent)
                self.parent = parent
                self.wert = ""
        def __del__(self):
                self.wait()
        def run(self):
                while True:
                        time.sleep(.2)
                        self.wert = str(self.parent.mukri())
                        self.emit( QtCore.SIGNAL('update(QString)'), self.wert )
                return
class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        Dialog.resize(400, 300)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("QDialog{Background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(255, 255, 255, 255));}")
                                
class Window(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent=parent)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.Konek_Arduino())
        self.ui.pushButton_2.clicked.connect(lambda: self.closer())
        self.ui.horizontalSlider.setEnabled(False)
        self.ui.horizontalSlider.valueChanged.connect(lambda: self.test())
    def test(self):
                self.ui.label_4.setText(str(self.ui.horizontalSlider.value()))
                if(self.ui.horizontalSlider.value()>=0):
                        self.ser.write(str(self.ui.horizontalSlider.value())+str("\r\n"))
    def MessageBox(self,title,message):
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle(title)
                msgBox.setText(message)
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.exec_()
    def mukri(self):
                buffer = ''
                        
                while True:
                        
                                buffer = buffer + self.ser.read(self.ser.inWaiting())
                                time.sleep(0.05)
                                if '\n' in buffer:
                                        lines = buffer.split('\n')
                                        last_received = lines.pop(0)
                                        buffer = '\n'.join(lines)
                                break
                return buffer

    def dummy(self,text):
                                self.ui.lcdNumber.display(str(text))
    def Konek_Arduino(self):
                try:
                        arduino_ports = [
                                p.device
                                for p in serial.tools.list_ports.comports()
                                if 'Arduino' in p.description
                                ]

                        self.ser = serial.Serial(arduino_ports[0], 9600, timeout=0.1)
                        time.sleep(1)
                        self.ui.pushButton.setEnabled(False)
                        self.ui.horizontalSlider.setEnabled(True)
                        self.workThread = Workthread(self)
                        self.connect( self.workThread, QtCore.SIGNAL("update(QString)"), self.dummy )
                        self.workThread.start()
                except:
                       if not arduino_ports:
                        self.MessageBox('PERINGATAN','Arduino tidak ditemukan!')
                                
                       if len(arduino_ports) > 1:
                            warnings.warn('Arduino lain ditemukan - Gunakan yang pertama!') 
                       sys.exit()
    def closer(self):
                    try:
                        self.ser.close();
                        self.close()
                    except:
                        self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = Window()
    myapp.show()
    sys.exit(app.exec_())

