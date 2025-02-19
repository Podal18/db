import pymysql
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication

from qq import Ui_Form as qqForm

class Ui_Form_auth(object):
    def setupUi(self, Form_auth):
        Form_auth.setObjectName("Form_auth")
        Form_auth.resize(400, 300)
        Form_auth.setStyleSheet("background-color: rgb(178, 195, 255);\n"
"font: 12pt \"Myanmar Text\";")
        self.vhodButton = QtWidgets.QPushButton(parent=Form_auth)
        self.vhodButton.setGeometry(QtCore.QRect(80, 230, 75, 23))
        self.vhodButton.setObjectName("vhodButton")
        self.vhodButton.clicked.connect(self.vhod)
        self.exButton = QtWidgets.QPushButton(parent=Form_auth)
        self.exButton.setGeometry(QtCore.QRect(210, 230, 75, 23))
        self.exButton.setObjectName("exButton")
        self.exButton.clicked.connect(QtWidgets.QApplication.quit)
        self.loginEdit = QtWidgets.QLineEdit(parent=Form_auth)
        self.loginEdit.setGeometry(QtCore.QRect(100, 70, 171, 21))
        self.loginEdit.setObjectName("loginEdit")
        self.pasEdit = QtWidgets.QLineEdit(parent=Form_auth)
        self.pasEdit.setGeometry(QtCore.QRect(100, 120, 171, 21))
        self.pasEdit.setObjectName("pasEdit")

        self.retranslateUi(Form_auth)
        QtCore.QMetaObject.connectSlotsByName(Form_auth)

    def retranslateUi(self, Form_auth):
        _translate = QtCore.QCoreApplication.translate
        Form_auth.setWindowTitle(_translate("Form_auth", "Авторизация"))
        self.vhodButton.setText(_translate("Form_auth", "вход"))
        self.exButton.setText(_translate("Form_auth", "выход"))
        self.loginEdit.setPlaceholderText(_translate("Form_auth", "логин"))
        self.pasEdit.setPlaceholderText(_translate("Form_auth", "пароль"))

    def vhod(self):
        loginn = self.loginEdit.text()
        passwordd = self.pasEdit.text()

        try:
            con =pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='worker',
                port=3309
            )

            with con.cursor() as cursor:
                sql = "select * from user where login=%s and password=%s"
                cursor.execute(sql, (loginn, passwordd))
                result = cursor.fetchone()

                if result:
                    print("qq")
                    self.popa()
                else:
                    print("error")

        except pymysql.MySQLError as e:
            print(str(e))

        finally:
            if con:
                con.close()


    def popa(self):
        self.winow = QtWidgets.QWidget()
        self.ui = qqForm()
        self.ui.setupUi(self.winow)
        self.winow.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_auth = QtWidgets.QWidget()
    ui = Ui_Form_auth()
    ui.setupUi(Form_auth)
    Form_auth.show()
    sys.exit(app.exec())
