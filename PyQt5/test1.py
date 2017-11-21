import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication,QLabel, QLineEdit,QTextEdit,QInputDialog
from PyQt5.QtGui import QIcon,QFont
import requests
import re
import random


class TsetTool(QWidget):
                              #super()方法返回了Example类的父类对象，并且我们调用了父类的构造方法。
    def __init__(self):            #def __init__(self, parent=None)   #也可以这样写
        super().__init__()         #super(Example, self).__init__(parent)

        self.main_UI()              #GUI的创建授予my_UI()方法完成。

    def main_UI(self):              #这些方法都是继承自QWidget类

        self.setToolTip('菜鸟写的，别问谁写的了')  # 调用setTooltip()方法创建提示框，提示框中可以使用富文本格式
        self.button = QPushButton('新建文件夹接口测试', self)  # 创建了一个按钮
        self.button.setToolTip('快点啊！你就能创建文件夹')  # 同样也给按钮设置提示框
        self.button.resize(self.button.sizeHint())  # 改变按钮大小，setHint()方法给了按钮一个推荐的大小
        self.button.move(50, 40)
        self.button.clicked.connect(self.test1)

        self.address = QPushButton('测试地址：',self)
        self.address.resize(self.address.sizeHint())
        self.address.move(180, 40)
        self.address.clicked.connect(self.showDialog1)

        self.addressEdit = QLineEdit('',self)
        self.addressEdit.resize(self.addressEdit.sizeHint())
        self.addressEdit.move(270, 40)

        self.name = QPushButton('用户名：', self)
        self.name.resize(self.name.sizeHint())
        self.name.move(180, 15)
        self.name.clicked.connect(self.nameshow)

        self.nameEdit = QLineEdit('', self)
        self.nameEdit.resize(self.nameEdit.sizeHint())
        self.nameEdit.move(270, 15)


        self.password = QPushButton('密码：', self)
        self.password.resize(self.password.sizeHint())
        self.password.move(420, 15)
        self.password.clicked.connect(self.passwordshow)

        self.passwordEdit = QLineEdit('', self)
        self.passwordEdit.resize(self.passwordEdit.sizeHint())
        self.passwordEdit.move(510, 15)

        self.setGeometry(450, 300, 650, 300)
        self.setWindowTitle('Lenovo Tset Tool')
        self.setWindowIcon(QIcon('logo.ico'))
        self.show()

    def showDialog1(self):
        text1, ok = QInputDialog.getText(self, '测试地址', '输入你的测试地址:')
        if ok:
            self.addressEdit.setText(str(text1))


    def nameshow(self):
        text2, ok = QInputDialog.getText(self, '用户名', '输入你的用户名:')
        if ok:
            self.nameEdit.setText(str(text2))

    def passwordshow(self):
        text3, ok = QInputDialog.getText(self, '密码', '输入你的密码:')
        if ok:
            self.passwordEdit.setText(str(text3))







    def test1(self):
        url = "http://172.16.52.138"
        url1 = url + "/v2/user/login"
        querystring = {"user_slug": "chrome", "password": "123456"}
        response1 = requests.request("post", url1, params=querystring)
        response2 = requests.request("post", url1, params=querystring).json()
        line0 = str(response1.cookies)
        line1 = str(response2)  # body
        var1 = str(re.findall(r"'uid': (.+?),", line1))
        line2 = str(re.sub(r"\W", "", var1))  # uid
        var2 = str(re.findall(r"'account_id': (.+?),", line1))
        line3 = str(re.sub(r"\W", "", var2))  # account_id
        var3 = str(re.findall(r'S=(.+?) ', line0))
        line4 = str(re.sub(r"\W", "", var3))  # S
        var4 = str(re.findall(r'SESS-ID=(.+?) ', line0))
        line5 = str(re.sub(r"\W", "", var4))  # SESS-ID
        var5 = str(re.findall(r'JSESSIONID=(.+?) ', line0))
        line6 = str(re.sub(r"\W", "", var5))  # JSESSIONID
        i = str(random.randint(0, 1000))
        url2 = url + "/v2/fileops/create_folder/databox/lenovo Test Tool" + i
        querystring2 = {"path_type": "self", "is_update": "false", "account_id": line3, "uid": line2,
                                    "S": line4, "X-LENOVO-SESS-ID": line5, "JSESSIONID": line6}
        response = requests.request("POST", url2, params=querystring2).json()



app = QApplication(sys.argv)
ex = TsetTool()
sys.exit(app.exec_())