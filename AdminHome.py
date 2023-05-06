

from PyQt5 import QtCore, QtGui, QtWidgets
from Training_CNN import build_cnn
import sys
from Prediction import Ui_Prediction

class Ui_AdminHome(object):

    def build_trainmodel(self):
        try:
            build_cnn()
            self.showMessageBox("Message", "Training model build successfully.")

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def detection(self):

        try:
            self.admn = QtWidgets.QDialog()
            self.ui = Ui_Prediction()
            self.ui.setupUi(self.admn)
            self.admn.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

   




    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(664, 599)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -30, 681, 631))
        self.label.setStyleSheet("background-image: url(../Detection/fic2.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 130, 341, 41))
        self.pushButton.setStyleSheet("font: 14pt \"Georgia\";\n"
"background-color: rgb(0, 85, 127);\n"
"color: rgb(225,225,225);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.build_trainmodel)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 230, 341, 41))
        self.pushButton_2.setStyleSheet("\n"
"font: 14pt \"Georgia\";\n"
"background-color: rgb(0, 85, 127);\n"
"color: rgb(225,225,225);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.detection)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AdminHome"))
        self.pushButton.setText(_translate("Dialog", "Build Training Model"))
        self.pushButton_2.setText(_translate("Dialog", "Crime Detection "))
       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Prediction()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
