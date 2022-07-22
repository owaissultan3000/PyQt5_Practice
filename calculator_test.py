from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from calculator import Ui_Calculator
import unittest
import sys
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5 import QtWidgets


class CalculatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.app = QApplication(sys.argv)
        self.Calculator = QtWidgets.QWidget()
        self.test : Ui_Calculator = Ui_Calculator(self.Calculator)
        self.btn_1, self.btn_2, self.sign_btn_plus, self.sign_btn_mul, self.equal_btn = self.get_input_buttons()

    def test_addition(self):
        QTest.mouseClick(self.btn_1, Qt.LeftButton)
        QTest.mouseClick(self.sign_btn_plus, Qt.LeftButton)
        QTest.mouseClick(self.btn_2, Qt.LeftButton)
        QTest.mouseClick(self.equal_btn, Qt.LeftButton)
        assert self.test.label.text() == "8"
        self.test.label.clear()


    def test_multiplication(self):
        QTest.mouseClick(self.btn_1, Qt.LeftButton)
        QTest.mouseClick(self.sign_btn_mul, Qt.LeftButton)
        QTest.mouseClick(self.btn_2, Qt.LeftButton)
        QTest.mouseClick(self.equal_btn, Qt.LeftButton)
        assert self.test.label.text() == "15"
        q

    def get_input_buttons(self) -> QPushButton:
        btn_1 = self.test.b3
        btn_2 = self.test.b5
        sign_btn_plus = self.test.b_plus
        sign_btn_mul = self.test.b_mul
        equal_btn = self.test.b_eq
        return btn_1, btn_2, sign_btn_plus, sign_btn_mul, equal_btn




if __name__ == '__main__':
    unittest.main()

