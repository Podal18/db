import pymysql
from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(719, 300)
        Form.setStyleSheet("background-color: rgb(178, 195, 255);\n"
"font: 12pt \"Myanmar Text\";")
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(90, 40, 161, 21))
        self.comboBox.setObjectName("comboBox")
        self.listWidget = QtWidgets.QListWidget(parent=Form)
        self.listWidget.setGeometry(QtCore.QRect(390, 40, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 240, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pp()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "выход"))

    def pp(self):
        try:
            con = pymysql.connect(
                host="localhost",
                user="root",
                password="root",
                database="worker",
                port=3309
            )
            with con.cursor() as cursor:
                cursor.execute("select id, name from dolzn")
                position = cursor.fetchall()

                for i in position:
                    self.comboBox.addItem(f"{i[0]} - {i[1]}")
                    self.listWidget.addItem(f"{i[0]} - {i[1]}")
        except pymysql.MySQLError as e:
            print(str(e))

        finally:
            if con:
                con.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
