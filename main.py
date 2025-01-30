from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import pymysql
import os
from PyQt6.QtWidgets import QListWidgetItem
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QSize

bd_con = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "test"
}

page = 5


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(377, 509)
        Form.setStyleSheet("background-color: rgb(212, 124, 255);"
                           )
        self.listWidget = QtWidgets.QListWidget(parent=Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 356, 450))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setIconSize(QSize(64, 64))

        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 480, 131, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.predidush)

        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 480, 131, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.listat)

        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(167, 475, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.n_p = 0
        self.zagruzka()
        self.cnt = 1
        self.label.setText(str(self.cnt))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", ">"))
        self.pushButton_2.setText(_translate("Form", "<"))

    def add_agent(self, offset):
        conn = pymysql.connect(**bd_con)
        cursor = conn.cursor()
        cursor.execute("SELECT agent.title as name, phone, logo, priority, agenttype.title "
                       "FROM agent INNER JOIN agenttype ON agent.agenttypeid = agenttype.id "
                       "ORDER BY priority DESC LIMIT %s OFFSET %s",
                        (page, offset))
        agents = cursor.fetchall()
        conn.close()
        return agents

    def zagruzka(self):
        self.listWidget.clear()
        agents = self.add_agent(self.n_p * page)

        for title, phone, logo, priority, a_t in agents:
            item = QListWidgetItem(f"{a_t} | {title} \n\n {phone} \n Приоритетность: {priority}\n")

            if not logo or logo.lower() in ["не указано", "отсутствует", "нет"]:
                logo_path = os.path.join(os.path.dirname(__file__), "picture.png")
            else:
                logo_path = os.path.join(os.path.dirname(__file__), logo)

            pixmap = QPixmap(logo_path)
            if pixmap.isNull():
                print(f"oshibka:{logo_path}")
            else:
                icon = QIcon(pixmap)
                item.setIcon(icon)

            self.listWidget.addItem(item)

    def listat(self):
        if self.n_p < 19:
            self.n_p += 1
            self.cnt += 1
            self.label.setText(str(self.cnt))
            self.zagruzka()

    def predidush(self):
        if self.n_p > 0:
            self.n_p -= 1
            self.cnt -= 1
            self.label.setText(str(self.cnt))
            self.zagruzka()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())