from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TodoApplication(object):
    def setupUi(self, TodoApplication):
        TodoApplication.setObjectName("TodoApplication")
        TodoApplication.resize(1000, 1000)
        TodoApplication.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(TodoApplication)
        self.label.setGeometry(QtCore.QRect(350, 60, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Add_Task_Button = QtWidgets.QPushButton(TodoApplication,clicked=lambda: self.add_task())
        self.Add_Task_Button.setGeometry(QtCore.QRect(750, 190, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Add_Task_Button.setFont(font)
        self.Add_Task_Button.setCheckable(False)
        self.Add_Task_Button.setChecked(False)
        self.Add_Task_Button.setObjectName("Add_Task_Button")
        self.Day_Label = QtWidgets.QLabel(TodoApplication)
        self.Day_Label.setGeometry(QtCore.QRect(80, 250, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Day_Label.setFont(font)
        self.Day_Label.setObjectName("Day_Label")
        self.Task_Input = QtWidgets.QLineEdit(TodoApplication)
        self.Task_Input.setGeometry(QtCore.QRect(270, 200, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Task_Input.setFont(font)
        self.Task_Input.setObjectName("Task_Input")
        self.Task_Label = QtWidgets.QLabel(TodoApplication)
        self.Task_Label.setGeometry(QtCore.QRect(80, 200, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Task_Label.setFont(font)
        self.Task_Label.setObjectName("Task_Label")
        self.Day_Input = QtWidgets.QLineEdit(TodoApplication)
        self.Day_Input.setGeometry(QtCore.QRect(270, 250, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Day_Input.setFont(font)
        self.Day_Input.setObjectName("Day_Input")
        self.Delete_Task_Button = QtWidgets.QPushButton(TodoApplication,clicked=lambda: self.delete_task())
        self.Delete_Task_Button.setGeometry(QtCore.QRect(745, 550, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Delete_Task_Button.setFont(font)
        self.Delete_Task_Button.setCheckable(False)
        self.Delete_Task_Button.setChecked(False)
        self.Delete_Task_Button.setObjectName("Delete_Task_Button")
        self.Clear_Button = QtWidgets.QPushButton(TodoApplication,clicked=lambda: self.clear_task())
        self.Clear_Button.setGeometry(QtCore.QRect(750, 250, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Clear_Button.setFont(font)
        self.Clear_Button.setCheckable(False)
        self.Clear_Button.setChecked(False)
        self.Clear_Button.setObjectName("Clear_Button")
        self.Complete_Task_Button = QtWidgets.QPushButton(TodoApplication,clicked=lambda: self.complete_task())
        self.Complete_Task_Button.setGeometry(QtCore.QRect(745, 700, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Complete_Task_Button.setFont(font)
        self.Complete_Task_Button.setCheckable(False)
        self.Complete_Task_Button.setChecked(False)
        self.Complete_Task_Button.setObjectName("Complete_Task_Button")
        self.listWidget = QtWidgets.QListWidget(TodoApplication)
        self.listWidget.setGeometry(QtCore.QRect(130, 420, 601, 501))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(TodoApplication)
        self.label_2.setGeometry(QtCore.QRect(370, 370, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(TodoApplication)
        QtCore.QMetaObject.connectSlotsByName(TodoApplication)

    def retranslateUi(self, TodoApplication):
        _translate = QtCore.QCoreApplication.translate
        TodoApplication.setWindowTitle(_translate("TodoApplication", "Form"))
        self.label.setText(_translate("TodoApplication", "TODO APP"))
        self.Add_Task_Button.setText(_translate("TodoApplication", "Add Task"))
        self.Day_Label.setText(_translate("TodoApplication", "Day & Time"))
        self.Task_Input.setPlaceholderText(_translate("TodoApplication", "Add Task"))
        self.Task_Label.setText(_translate("TodoApplication", "Add Task"))
        self.Day_Input.setPlaceholderText(_translate("TodoApplication", "Add Day & Time"))
        self.Delete_Task_Button.setText(_translate("TodoApplication", "Delete Task"))
        self.Clear_Button.setText(_translate("TodoApplication", "Clear"))
        self.Complete_Task_Button.setText(_translate("TodoApplication", "Complete Task"))
        self.label_2.setText(_translate("TodoApplication", "All Tasks"))

    def add_task(self):
        # print(self.Task_Input.text())
        # print(self.Day_Input.text())
        task = self.Task_Input.text()
        day_time = self.Day_Input.text()
        data = task + " ( " + day_time + " )"
        self.listWidget.addItem(data)
        self.Task_Input.clear()
        self.Day_Input.clear()
        data = ""

    def clear_task(self):
        self.Task_Input.clear()
        self.Day_Input.clear()

    def delete_task(self):
        selected = self.listWidget.currentRow()
        self.listWidget.takeItem(selected)

    def complete_task(self):
        selected = self.listWidget.currentRow()
        self.listWidget.takeItem(selected)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TodoApplication = QtWidgets.QWidget()
    ui = Ui_TodoApplication()
    ui.setupUi(TodoApplication)
    TodoApplication.show()
    sys.exit(app.exec_())