import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
    QLineEdit, QListView, QFormLayout, QListWidget, QMenuBar
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(800, 200, 1000, 1000)
        self.setWindowTitle("Todo Application")
        header_label = QtWidgets.QLabel("TODO APP", alignment=Qt.AlignHCenter)
        header_label.move(700, 90)
        header_label.setFont(QFont('Arial', 18, QFont.Bold))

        task_label = QtWidgets.QLabel("Task")
        task_label.setFont(QFont('Arial', 12, QFont.Bold))
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Add Task")
        self.task_input.setFont(QFont('Arial', 12))
        task_label.move(300, 100)

        day_label = QtWidgets.QLabel("Day & Time")
        day_label.setFont(QFont('Arial', 12, QFont.Bold))
        self.day_input = QLineEdit()
        self.day_input.setPlaceholderText("Add Day & Time")
        self.day_input.setFont(QFont('Arial', 12))

        add_task = QtWidgets.QPushButton("Add Task", clicked=lambda: self.add_task())
        add_task.setFont(QFont('Arial', 12, QFont.Bold))

        clear_task = QtWidgets.QPushButton("Clear", clicked=lambda: self.clear_task())
        clear_task.setFont(QFont('Arial', 12, QFont.Bold))

        self.all_task = QListWidget()
        self.all_task.setFont((QFont('Arial', 12, QFont.Bold)))
        delete_task = QtWidgets.QPushButton("Delete Task", clicked=lambda: self.delete_task())
        delete_task.setFont(QFont('Arial', 12, QFont.Bold))

        complete_task = QtWidgets.QPushButton("Complete Task", clicked=lambda: self.complete_task())
        complete_task.setFont(QFont('Arial', 12, QFont.Bold))

        form_layout = QFormLayout()
        self.setLayout(form_layout)

        form_layout.addRow(header_label)
        form_layout.addRow(task_label, self.task_input)
        form_layout.addRow(day_label, self.day_input)
        form_layout.addRow(add_task)
        form_layout.addRow(clear_task)
        form_layout.addRow(self.all_task)
        form_layout.addRow(complete_task)
        form_layout.addRow(delete_task)
        self.show()

    def add_task(self):
        task = self.task_input.text()
        day_time = self.day_input.text()
        data = task + " ( " + day_time + " )"
        self.all_task.addItem(data)
        self.task_input.clear()
        self.day_input.clear()
        data = ""

    def clear_task(self):
        self.task_input.clear()
        self.day_input.clear()

    def delete_task(self):
        selected = self.all_task.currentRow()
        self.all_task.takeItem(selected)

    def complete_task(self):
        selected = self.all_task.currentRow()
        self.all_task.takeItem(selected)


app = QApplication([])

window = MainWindow()

app.exec()
