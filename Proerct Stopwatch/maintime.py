from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from timer import Ui_Dialog

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(788, 772)
        self.jam = QtWidgets.QTextBrowser(Dialog)
        self.jam.setGeometry(QtCore.QRect(150, 160, 151, 101))
        self.jam.setObjectName("jam")
        self.menit = QtWidgets.QTextBrowser(Dialog)
        self.menit.setGeometry(QtCore.QRect(310, 160, 151, 101))
        self.menit.setObjectName("menit")
        self.detik = QtWidgets.QTextBrowser(Dialog)
        self.detik.setGeometry(QtCore.QRect(470, 160, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.detik.setFont(font)
        self.detik.setObjectName("detik")
        self.Lap = QtWidgets.QPushButton(Dialog)
        self.Lap.setGeometry(QtCore.QRect(540, 330, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Lap.setFont(font)
        self.Lap.setObjectName("Lap")
        self.Mulaistop = QtWidgets.QPushButton(Dialog)
        self.Mulaistop.setGeometry(QtCore.QRect(310, 330, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Mulaistop.setFont(font)
        self.Mulaistop.setObjectName("Mulaistop")
        self.LayarLap = QtWidgets.QTextBrowser(Dialog)
        self.LayarLap.setGeometry(QtCore.QRect(80, 430, 601, 291))
        self.LayarLap.setObjectName("LayarLap")
        self.keluar = QtWidgets.QPushButton(Dialog)
        self.keluar.setGeometry(QtCore.QRect(80, 330, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.keluar.setFont(font)
        self.keluar.setObjectName("keluar")

        self.retranslateUi(Dialog)
        self.keluar.clicked.connect(Dialog.close)  # Change to close the dialog
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Stopwatch"))
        self.Lap.setText(_translate("Dialog", "Lap"))
        self.Mulaistop.setText(_translate("Dialog", "Mulai/Stop"))
        self.keluar.setText(_translate("Dialog", "Keluar"))

class StopwatchApp(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_display)

        self.elapsed_time = 0
        self.running = False

        self.Mulaistop.clicked.connect(self.start_stop)
        self.Lap.clicked.connect(self.record_lap)

    def start_stop(self):
        if self.running:
            self.timer.stop()
        else:
            self.timer.start(1000)
        self.running = not self.running

    def update_display(self):
        self.elapsed_time += 1
        hours, remainder = divmod(self.elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.jam.setText(f'{hours:02d}')
        self.menit.setText(f'{minutes:02d}')
        self.detik.setText(f'{seconds:02d}')

    def record_lap(self):
        hours, remainder = divmod(self.elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        lap_time = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
        self.LayarLap.append(lap_time)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = StopwatchApp()
    dialog.show()
    sys.exit(app.exec_())
