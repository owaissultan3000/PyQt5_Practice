from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import math


class Ui_Calculator(object):
    def __init__(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(500, 700)
        self.b_ln = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("ln"))
        self.b_ln.setGeometry(QtCore.QRect(20, 640, 71, 51))
        self.b_ln.setObjectName("b_ln")

        self.b_pm = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("-1"))
        self.b_pm.setGeometry(QtCore.QRect(120, 640, 71, 51))
        self.b_pm.setObjectName("b_pm")

        self.b0 = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("0"))
        self.b0.setGeometry(QtCore.QRect(220, 640, 71, 51))
        self.b0.setObjectName("b0")

        self.b_dot = QtWidgets.QPushButton(Calculator, clicked=lambda: self.action_point())
        self.b_dot.setGeometry(QtCore.QRect(320, 640, 71, 51))
        self.b_dot.setObjectName("b_dot")

        self.b_eq = QtWidgets.QPushButton(Calculator, clicked=lambda: self.action_equal())
        self.b_eq.setGeometry(QtCore.QRect(420, 640, 71, 51))
        self.b_eq.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                "background-color: rgb(105, 105, 105);")
        self.b_eq.setObjectName("b_eq")

        self.b3 = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("3"))
        self.b3.setGeometry(QtCore.QRect(320, 570, 71, 51))
        self.b3.setObjectName("b3")

        self.b2 = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("2"))
        self.b2.setGeometry(QtCore.QRect(220, 570, 71, 51))
        self.b2.setObjectName("b2")

        self.b_log = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("log"))
        self.b_log.setGeometry(QtCore.QRect(20, 570, 71, 51))
        self.b_log.setObjectName("b_log")

        self.b_plus = QtWidgets.QPushButton(Calculator, clicked=lambda: self.action_plus())
        self.b_plus.setGeometry(QtCore.QRect(420, 570, 71, 51))
        self.b_plus.setObjectName("b_plus")

        self.b1 = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("1"))
        self.b1.setGeometry(QtCore.QRect(120, 570, 71, 51))
        self.b1.setObjectName("b1")

        self.b7 = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("7"))
        self.b7.setGeometry(QtCore.QRect(120, 430, 71, 51))
        self.b7.setObjectName("b7")

        self.b6 = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("6"))
        self.b6.setGeometry(QtCore.QRect(320, 500, 71, 51))
        self.b6.setObjectName("b6")

        self.b8 = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("8"))
        self.b8.setGeometry(QtCore.QRect(220, 430, 71, 51))
        self.b8.setObjectName("b8")

        self.b9 = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("9"))
        self.b9.setGeometry(QtCore.QRect(320, 430, 71, 51))
        self.b9.setObjectName("b9")

        self.b_mul = QtWidgets.QPushButton(Calculator, clicked=lambda: self.action_mul())
        self.b_mul.setGeometry(QtCore.QRect(420, 430, 71, 51))
        self.b_mul.setObjectName("b_mul")

        self.b5 = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("5"))
        self.b5.setGeometry(QtCore.QRect(220, 500, 71, 51))
        self.b5.setObjectName("b5")

        self.b_10x = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("10^x"))
        self.b_10x.setGeometry(QtCore.QRect(20, 500, 71, 51))
        self.b_10x.setObjectName("b_10x")

        self.b_subt = QtWidgets.QPushButton(Calculator, clicked=lambda: self.action_minus())
        self.b_subt.setGeometry(QtCore.QRect(420, 500, 71, 51))
        self.b_subt.setObjectName("b_subt")

        self.b_xpowy = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("x^y"))
        self.b_xpowy.setGeometry(QtCore.QRect(20, 430, 71, 51))
        self.b_xpowy.setObjectName("b_xpowy")

        self.b4 = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("4"))
        self.b4.setGeometry(QtCore.QRect(120, 500, 71, 51))
        self.b4.setObjectName("b4")

        self.b_bo = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("("))
        self.b_bo.setGeometry(QtCore.QRect(120, 360, 71, 51))
        self.b_bo.setObjectName("b_bo")

        self.b_pie = QtWidgets.QPushButton(Calculator, clicked=lambda: self.action_pie())
        self.b_pie.setGeometry(QtCore.QRect(120, 220, 71, 51))
        self.b_pie.setObjectName("b_pie")

        self.b_bar = QtWidgets.QPushButton(Calculator, clicked=lambda: self.action_abs())
        self.b_bar.setGeometry(QtCore.QRect(220, 290, 71, 51))
        self.b_bar.setObjectName("b_bar")

        self.b_1overx = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("1/x"))
        self.b_1overx.setGeometry(QtCore.QRect(120, 290, 71, 51))
        self.b_1overx.setObjectName("b_1overx")

        self.b_bc = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation(")"))
        self.b_bc.setGeometry(QtCore.QRect(220, 360, 71, 51))
        self.b_bc.setObjectName("b_bc")

        self.b_2nd = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("2nd"))
        self.b_2nd.setGeometry(QtCore.QRect(20, 220, 71, 51))
        self.b_2nd.setObjectName("b_2nd")

        self.b_fac = QtWidgets.QPushButton(Calculator, clicked=lambda: self.action_fac())
        self.b_fac.setGeometry(QtCore.QRect(320, 360, 71, 51))
        self.b_fac.setObjectName("b_fac")

        self.b_div = QtWidgets.QPushButton(Calculator, clicked=lambda: self.action_div())
        self.b_div.setGeometry(QtCore.QRect(420, 360, 71, 51))
        self.b_div.setObjectName("b_div")

        self.pushButton_29 = QtWidgets.QPushButton(Calculator, clicked=lambda: self.action_square())
        self.pushButton_29.setGeometry(QtCore.QRect(20, 290, 71, 51))
        self.pushButton_29.setObjectName("b_sq")

        self.b_del = QtWidgets.QPushButton(Calculator, clicked=lambda: self.action_del())
        self.b_del.setGeometry(QtCore.QRect(420, 220, 71, 51))
        self.b_del.setObjectName("b_del")

        self.b_exp_2 = QtWidgets.QPushButton(Calculator, clicked=lambda: self.action_exp())
        self.b_exp_2.setGeometry(QtCore.QRect(220, 220, 71, 51))
        self.b_exp_2.setObjectName("b_exp_2")

        self.b_exp = QtWidgets.QPushButton(Calculator)
        self.b_exp.setGeometry(QtCore.QRect(319, 290, 71, 51))
        self.b_exp.setObjectName("b_exp")

        self.b_1over2 = QtWidgets.QPushButton(Calculator)
        self.b_1over2.setGeometry(QtCore.QRect(20, 360, 71, 51))
        self.b_1over2.setObjectName("b_1over2")

        self.b_mod = QtWidgets.QPushButton(Calculator)
        self.b_mod.setGeometry(QtCore.QRect(420, 290, 71, 51))
        self.b_mod.setObjectName("b_mod")

        self.b_CE = QtWidgets.QPushButton(Calculator, clicked=lambda: self.calcuation("CE"))
        self.b_CE.setGeometry(QtCore.QRect(320, 220, 71, 51))
        self.b_CE.setObjectName("b_CE")

        self.label = QtWidgets.QLabel(Calculator)
        self.label.setGeometry(QtCore.QRect(20, 130, 471, 51))
        self.label.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def calcuation(self, key):
        if key == "CE":
            self.label.setText("0")
        else:
            if self.label.text() == "0":
                self.label.setText("")
            self.label.setText(f'{self.label.text()}{key}')

    def action_equal(self):

        # get the label text
        equation = self.label.text()

        try:
            # getting the ans
            ans = eval(equation)

            # setting text to the label
            self.label.setText(str(ans))

        except:
            # setting text to the label
            self.label.setText("Wrong Input")

    def action_plus(self):
        text = self.label.text()
        self.label.setText(text + " + ")

    def action_minus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " - ")

    def action_div(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " / ")

    def action_mul(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " * ")

    def action_point(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + ".")

    def action_del(self):
        # clearing a single digit
        text = self.label.text()
        self.label.setText(text[:len(text) - 1])

    def action_square(self):
        text = float(self.label.text())
        self.label.setText(str(text * text))

    def action_abs(self):
        text = float(self.label.text())
        self.label.setText(str(text * (-1)))

    def action_pie(self):
        self.label.setText("3.14159")

    def action_exp(self):
        self.label.setText("2.7182")

    def action_fac(self):
        text = float(self.label.text())
        if text == 0.0:
            self.label.setText("1")
        else:
            self.label.setText(str(math.gamma(text + 1)))

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Form"))
        self.b_ln.setText(_translate("Calculator", "ln"))
        self.b_pm.setText(_translate("Calculator", "+/-"))
        self.b0.setText(_translate("Calculator", "0"))
        self.b_dot.setText(_translate("Calculator", "."))
        self.b_eq.setText(_translate("Calculator", "="))
        self.b3.setText(_translate("Calculator", "3"))
        self.b2.setText(_translate("Calculator", "2"))
        self.b_log.setText(_translate("Calculator", "log"))
        self.b_plus.setText(_translate("Calculator", "+"))
        self.b1.setText(_translate("Calculator", "1"))
        self.b7.setText(_translate("Calculator", "7"))
        self.b6.setText(_translate("Calculator", "6"))
        self.b8.setText(_translate("Calculator", "8"))
        self.b9.setText(_translate("Calculator", "9"))
        self.b_mul.setText(_translate("Calculator", "X"))
        self.b5.setText(_translate("Calculator", "5"))
        self.b_10x.setText(_translate("Calculator", "10^x"))
        self.b_subt.setText(_translate("Calculator", "-"))
        self.b_xpowy.setText(_translate("Calculator", "x^y"))
        self.b4.setText(_translate("Calculator", "4"))
        self.b_bo.setText(_translate("Calculator", "("))
        self.b_pie.setText(_translate("Calculator", "pie"))
        self.b_bar.setText(_translate("Calculator", "|x|"))
        self.b_1overx.setText(_translate("Calculator", "1/x"))
        self.b_bc.setText(_translate("Calculator", ")"))
        self.b_2nd.setText(_translate("Calculator", "2nd"))
        self.b_fac.setText(_translate("Calculator", "n!"))
        self.b_div.setText(_translate("Calculator", "/"))
        self.pushButton_29.setText(_translate("Calculator", "x^2"))
        self.b_del.setText(_translate("Calculator", "del"))
        self.b_exp_2.setText(_translate("Calculator", "e"))
        self.b_exp.setText(_translate("Calculator", "exp"))
        self.b_1over2.setText(_translate("Calculator", "x^1/2"))
        self.b_mod.setText(_translate("Calculator", "mod"))
        self.b_CE.setText(_translate("Calculator", "CE"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QWidget()
    ui = Ui_Calculator(Calculator)
    # ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
