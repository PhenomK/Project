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
        button = QPushButton('新建文件夹接口测试', self)  # 创建了一个按钮
        button.setToolTip('快点啊！你就能创建文件夹')  # 同样也给按钮设置提示框
        button.resize(button.sizeHint())  # 改变按钮大小，setHint()方法给了按钮一个推荐的大小
        button.move(50, 40)
        button.clicked.connect(self.test1)

        address = QLabel('测试地址：',self)
        address.resize(address.sizeHint())
        address.move(200, 45)
        #address.clicked.connect(self.showDialog1)
        addressEdit = QLineEdit('http://',self)
        addressEdit.resize(addressEdit.sizeHint())
        addressEdit.move(270, 40)


        #def showDialog1(self):
        #text, ok = QInputDialog.getText(self, '测试地址', '输入你的测试地址:')
        #if ok:
             #self.titleEdit.setText(str(text))



        title1 = QLabel('用户名：', self)
        title1.resize(title1.sizeHint())
        title1.move(200, 20)
        titleEdit1 = QLineEdit('admin', self)
        titleEdit1.resize(titleEdit1.sizeHint())
        titleEdit1.move(270, 15)


        title2 = QLabel('密码：', self)
        title2.resize(title1.sizeHint())
        title2.move(420, 20)
        titleEdit2 = QLineEdit('123456', self)
        titleEdit2.resize(titleEdit2.sizeHint())
        titleEdit2.move(460, 15)

        self.setGeometry(450, 300, 600, 300)
        self.setWindowTitle('Lenovo Tset Tool')
        self.setWindowIcon(QIcon('logo.ico'))
        self.show()



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