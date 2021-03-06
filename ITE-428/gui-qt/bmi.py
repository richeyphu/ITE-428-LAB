# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bmi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frm_bmi(object):
    def setupUi(self, frm_bmi):
        frm_bmi.setObjectName("frm_bmi")
        frm_bmi.resize(400, 300)
        self.lbl_weight = QtWidgets.QLabel(frm_bmi)
        self.lbl_weight.setGeometry(QtCore.QRect(30, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.lbl_weight.setFont(font)
        self.lbl_weight.setObjectName("lbl_weight")
        self.lbl_height = QtWidgets.QLabel(frm_bmi)
        self.lbl_height.setGeometry(QtCore.QRect(30, 80, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.lbl_height.setFont(font)
        self.lbl_height.setObjectName("lbl_height")
        self.lbl_bmi = QtWidgets.QLabel(frm_bmi)
        self.lbl_bmi.setGeometry(QtCore.QRect(230, 150, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.lbl_bmi.setFont(font)
        self.lbl_bmi.setText("")
        self.lbl_bmi.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_bmi.setObjectName("lbl_bmi")
        self.txt_weight = QtWidgets.QTextEdit(frm_bmi)
        self.txt_weight.setGeometry(QtCore.QRect(230, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_weight.setFont(font)
        self.txt_weight.setObjectName("txt_weight")
        self.txt_height = QtWidgets.QTextEdit(frm_bmi)
        self.txt_height.setGeometry(QtCore.QRect(230, 80, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_height.setFont(font)
        self.txt_height.setObjectName("txt_height")
        self.btn_calculate = QtWidgets.QPushButton(frm_bmi)
        self.btn_calculate.setGeometry(QtCore.QRect(30, 130, 161, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.btn_calculate.setFont(font)
        self.btn_calculate.setObjectName("btn_calculate")
        self.btn_reset = QtWidgets.QPushButton(frm_bmi)
        self.btn_reset.setGeometry(QtCore.QRect(30, 210, 161, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.btn_reset.setFont(font)
        self.btn_reset.setObjectName("btn_reset")

        self.retranslateUi(frm_bmi)
        QtCore.QMetaObject.connectSlotsByName(frm_bmi)

        # Event-Driven
        self.btn_calculate.clicked.connect(self.cal)
        self.btn_reset.clicked.connect(self.clear)

    def cal(self):
        # print("Test Success")
        try:
            w = float(self.txt_weight.toPlainText())
            h = float(self.txt_height.toPlainText())
            bmi = w / ((h / 100) ** 2)
            self.lbl_bmi.setText("{:.2f}".format(bmi))
        except Exception as e:
            print(e)

    def clear(self):
        self.lbl_bmi.setText("")
        self.txt_weight.setText("")
        self.txt_height.setText("")
        self.txt_weight.setFocus()

    def retranslateUi(self, frm_bmi):
        _translate = QtCore.QCoreApplication.translate
        frm_bmi.setWindowTitle(_translate("frm_bmi", "????????????????????????????????????????????? BMI"))
        self.lbl_weight.setText(_translate("frm_bmi", "????????????????????????????????? (Kg)"))
        self.lbl_height.setText(_translate("frm_bmi", "????????????????????????????????? (??????.)"))
        self.btn_calculate.setText(_translate("frm_bmi", "???????????????????????? BMI"))
        self.btn_reset.setText(_translate("frm_bmi", "???????????????????????????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frm_bmi = QtWidgets.QDialog()
    ui = Ui_frm_bmi()
    ui.setupUi(frm_bmi)
    frm_bmi.show()
    sys.exit(app.exec_())
