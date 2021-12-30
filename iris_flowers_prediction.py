# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iris_flowers_prediction.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 549)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 20, 331, 41))
        self.label.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 171, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 210, 161, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 280, 151, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 350, 161, 51))
        self.label_5.setObjectName("label_5")
        self.le_sl = QtWidgets.QLineEdit(self.centralwidget)
        self.le_sl.setGeometry(QtCore.QRect(220, 150, 261, 31))
        self.le_sl.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(214, 214, 214);")
        self.le_sl.setText("")
        self.le_sl.setAlignment(QtCore.Qt.AlignCenter)
        self.le_sl.setObjectName("le_sl")
        self.le_sw = QtWidgets.QLineEdit(self.centralwidget)
        self.le_sw.setGeometry(QtCore.QRect(220, 220, 261, 31))
        self.le_sw.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.le_sw.setAlignment(QtCore.Qt.AlignCenter)
        self.le_sw.setObjectName("le_sw")
        self.le_pl = QtWidgets.QLineEdit(self.centralwidget)
        self.le_pl.setGeometry(QtCore.QRect(220, 290, 261, 31))
        self.le_pl.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.le_pl.setAlignment(QtCore.Qt.AlignCenter)
        self.le_pl.setObjectName("le_pl")
        self.le_pw = QtWidgets.QLineEdit(self.centralwidget)
        self.le_pw.setGeometry(QtCore.QRect(220, 360, 261, 31))
        self.le_pw.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.le_pw.setAlignment(QtCore.Qt.AlignCenter)
        self.le_pw.setObjectName("le_pw")
        self.lbl_classe = QtWidgets.QLabel(self.centralwidget)
        self.lbl_classe.setGeometry(QtCore.QRect(500, 120, 331, 291))
        self.lbl_classe.setText("")
        self.lbl_classe.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_classe.setObjectName("lbl_classe")
        self.btn_predict = QtWidgets.QPushButton(self.centralwidget)
        self.btn_predict.setGeometry(QtCore.QRect(190, 470, 141, 41))
        self.btn_predict.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(141, 141, 141);")
        self.btn_predict.setObjectName("btn_predict")
        self.btn_quit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_quit.setGeometry(QtCore.QRect(480, 470, 141, 41))
        self.btn_quit.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(141, 141, 141);")
        self.btn_quit.setObjectName("btn_quit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fleurs d\'Iris"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Iris flowers Prediction</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Sepal Length :</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Sepal Width :</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Petal Length :</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Petal Width :</span></p></body></html>"))
        self.btn_predict.setText(_translate("MainWindow", "PREDICT"))
        self.btn_quit.setText(_translate("MainWindow", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

