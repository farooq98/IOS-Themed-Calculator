# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calcultor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calcultor(object):
    def setupUi(self, Calcultor):
        Calcultor.setObjectName("Calcultor")
        Calcultor.setWindowModality(QtCore.Qt.NonModal)
        Calcultor.resize(266, 381)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Calcultor.sizePolicy().hasHeightForWidth())
        Calcultor.setSizePolicy(sizePolicy)
        Calcultor.setMinimumSize(QtCore.QSize(266, 381))
        Calcultor.setMaximumSize(QtCore.QSize(266, 381))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Calculator_5122x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Calcultor.setWindowIcon(icon)
        Calcultor.setWindowOpacity(1.0)
        Calcultor.setStyleSheet("#frame{\n"
"    background-color: rgb(0,0,0);\n"
"}\n"
"#lineEdit{\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: 0px;\n"
"}\n"
"#pushButton{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(63,63,63);\n"
"    color: white;\n"
"}\n"
"\n"
"#pushButton_2{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(63,63,63);\n"
"    color: white;\n"
"}\n"
"#pushButton_3{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(63,63,63);\n"
"    color: white;\n"
"}\n"
"#pushButton_4{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(63,63,63);\n"
"    color: white;\n"
"}\n"
"#pushButton_5{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(63,63,63);\n"
"    color: white;\n"
"}\n"
"#pushButton_6{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(63,63,63);\n"
"    color: white;\n"
"}\n"
"#pushButton_7{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(63,63,63);\n"
"    color: white;\n"
"}\n"
"#pushButton_8{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(63,63,63);\n"
"    color: white;\n"
"}\n"
"#pushButton_9{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(63,63,63);\n"
"    color: white;\n"
"}\n"
"#pushButton_10{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(63,63,63);\n"
"    color: white;\n"
"}\n"
"#pushButton_11{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(63,63,63);\n"
"    color: white;\n"
"}\n"
"#pushButton_12{\n"
"    border-radius: 25px;\n"
"    background-color: orange;\n"
"    color: white;\n"
"}\n"
"#pushButton_13{\n"
"    border-radius: 25px;\n"
"    background-color: orange;\n"
"    color: white;\n"
"}\n"
"#pushButton_14{\n"
"    border-radius: 25px;\n"
"    background-color: orange;\n"
"    color: white;\n"
"}\n"
"#pushButton_15{\n"
"    border-radius: 25px;\n"
"    background-color: orange;\n"
"    color: white;\n"
"}\n"
"#pushButton_16{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(162,162,162);\n"
"}\n"
"#pushButton_17{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(162,162,162);\n"
"}\n"
"#pushButton_18{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(162,162,162);\n"
"}\n"
"#pushButton_19{\n"
"    border-radius: 25px;\n"
"    background-color: orange;\n"
"    color: white;\n"
"}\n"
"#pushButton:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(115,115,115);\n"
"    color: white;\n"
"}\n"
"\n"
"#pushButton_2:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(115,115,115);\n"
"    color: white;\n"
"}\n"
"#pushButton_3:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(115,115,115);\n"
"    color: white;\n"
"}\n"
"#pushButton_4:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(115,115,115);\n"
"    color: white;\n"
"}\n"
"#pushButton_5:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(115,115,115);\n"
"    color: white;\n"
"}\n"
"#pushButton_6:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(115,115,115);\n"
"    color: white;\n"
"}\n"
"#pushButton_7:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(115,115,115);\n"
"    color: white;\n"
"}\n"
"#pushButton_8:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(115,115,115);\n"
"    color: white;\n"
"}\n"
"#pushButton_9:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(115,115,115);\n"
"    color: white;\n"
"}\n"
"#pushButton_10:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(115,115,115);\n"
"    color: white;\n"
"}\n"
"#pushButton_11:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(115,115,115);\n"
"    color: white;\n"
"}\n"
"#pushButton_12:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(244,201,149);\n"
"    color: white;\n"
"}\n"
"#pushButton_13:hover{\n"
"    border-radius: 25px;\n"
"    background-color:rgb(244,201,149);\n"
"    color: white;\n"
"}\n"
"#pushButton_14:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(244,201,149);\n"
"    color: white;\n"
"}\n"
"#pushButton_15:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(244,201,149);\n"
"    color: white;\n"
"}\n"
"#pushButton_19:hover{\n"
"    border-radius: 25px;\n"
"    background-color:  rgb(244,201,149);\n"
"    color: white;\n"
"}\n"
"#pushButton_16:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(217,217,217);\n"
"}\n"
"#pushButton_17:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(217,217,217);\n"
"}\n"
"#pushButton_18:hover{\n"
"    border-radius: 25px;\n"
"    background-color: rgb(217,217,217);\n"
"}")
        Calcultor.setWindowFilePath("")
        self.frame = QtWidgets.QFrame(Calcultor)
        self.frame.setGeometry(QtCore.QRect(-11, -1, 371, 391))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 190, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 190, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 250, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(90, 250, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 310, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(150, 250, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(150, 190, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(150, 310, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(210, 310, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(210, 250, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(210, 190, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(210, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setGeometry(QtCore.QRect(30, 70, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setGeometry(QtCore.QRect(90, 70, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame)
        self.pushButton_18.setGeometry(QtCore.QRect(150, 70, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame)
        self.pushButton_19.setGeometry(QtCore.QRect(210, 70, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")

        self.retranslateUi(Calcultor)
        QtCore.QMetaObject.connectSlotsByName(Calcultor)

    def retranslateUi(self, Calcultor):
        _translate = QtCore.QCoreApplication.translate
        Calcultor.setWindowTitle(_translate("Calcultor", "Calcultor"))
        self.lineEdit.setText(_translate("Calcultor", "0"))
        self.pushButton.setText(_translate("Calcultor", "7"))
        self.pushButton_2.setText(_translate("Calcultor", "4"))
        self.pushButton_3.setText(_translate("Calcultor", "8"))
        self.pushButton_4.setText(_translate("Calcultor", "5"))
        self.pushButton_5.setText(_translate("Calcultor", "1"))
        self.pushButton_6.setText(_translate("Calcultor", "2"))
        self.pushButton_7.setText(_translate("Calcultor", "0"))
        self.pushButton_8.setText(_translate("Calcultor", "9"))
        self.pushButton_9.setText(_translate("Calcultor", "3"))
        self.pushButton_10.setText(_translate("Calcultor", "6"))
        self.pushButton_11.setText(_translate("Calcultor", "."))
        self.pushButton_12.setText(_translate("Calcultor", "="))
        self.pushButton_13.setText(_translate("Calcultor", "+"))
        self.pushButton_14.setText(_translate("Calcultor", "-"))
        self.pushButton_15.setText(_translate("Calcultor", "x"))
        self.pushButton_16.setText(_translate("Calcultor", "AC"))
        self.pushButton_17.setText(_translate("Calcultor", "sin"))
        self.pushButton_18.setText(_translate("Calcultor", "%"))
        self.pushButton_19.setText(_translate("Calcultor", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calcultor = QtWidgets.QDialog()
    ui = Ui_Calcultor()
    ui.setupUi(Calcultor)
    Calcultor.show()
    sys.exit(app.exec_())
