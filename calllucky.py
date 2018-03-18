import sys
import threading
import time

from PyQt5.QtGui import QPalette, QColor, QFont, QIcon, QBrush
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog

from lucky import Ui_Form


class LuckyForm(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(LuckyForm, self).__init__(parent)

        self.flag = False
        self.count = 0
        self.initData()
        self.setupUi(self)
        self.initView()
        self.list_check = []



    def initData(self):
        self.data = ["宋江", "卢俊义", "魏定国 ", "欧 鹏", "燕 顺", "凌 振", "蒋 敬", "吕 方", "郭 盛", "安道全", "皇甫端 ", "王 英 ", "扈三娘", "孔 亮", "孙悟空", "猪八戒", "唐僧"]
        #  self.data = []

    def initView(self):

        self.setWindowIcon(QIcon("images/timg.jpg"))
        self.setWindowTitle("抽奖系统")
        self.roll.clicked.connect(self.roll_click)
        self.stop.clicked.connect(self.stop_click)
        self.add.clicked.connect(self.add_message)
        # 设置背景
        self.palette = QPalette()
        background_color = QColor()
        background_color.setNamedColor('#88ff0000')
        self.palette.setColor(QPalette.Window, background_color)
        self.show_name.setPalette(self.palette)

        palette1 = QPalette()
        palette1.setColor(self.backgroundRole(), QColor(192,253,123))   # 设置背景颜色
        self.setPalette(palette1)

        self.label.setPalette(self.palette)
        self.label_2.setPalette(self.palette)
        self.label_3.setPalette(self.palette)
        self.label_4.setPalette(self.palette)
        self.label_5.setPalette(self.palette)
        self.label_6.setPalette(self.palette)
        self.label_7.setPalette(self.palette)
        self.label_8.setPalette(self.palette)
        self.label_9.setPalette(self.palette)
        self.label_10.setPalette(self.palette)
        self.label_11.setPalette(self.palette)
        self.label_12.setPalette(self.palette)

        self.label_14.setPalette(self.palette)
        self.label_15.setPalette(self.palette)
        self.label_16.setPalette(self.palette)
        self.label_17.setPalette(self.palette)
        self.label_18.setPalette(self.palette)
        self.label_19.setPalette(self.palette)
        self.label_20.setPalette(self.palette)
        self.label_21.setPalette(self.palette)
        self.label_22.setPalette(self.palette)





    def add_message(self):
        self.addText()
        print("------------add---------")

    def roll_click(self):
        self.flag = True
        self.t = threading.Thread(target=self.start_roll, name='start_roll')
        self.t.start()



    def start_roll(self):
        print("stop-------------------")
        print(self.data)
        while self.flag:
            for item in self.data:
                if not self.flag:
                    self.set_show()
                    return
                time.sleep(0.06)
                print(self.show_name.setText(item))
    def set_show(self):
        self.list_check.append(self.show_name.text())
        self.data.remove(self.show_name.text())
        self.count += 1
        if self.count == 1:
            self.label_4.setText(self.show_name.text())
        elif self.count == 2:
            self.label_5.setText(self.show_name.text())
        elif self.count == 3:
            self.label_7.setText(self.show_name.text())
        elif self.count == 4:
            self.label_8.setText(self.show_name.text())
        elif self.count == 5:
            self.label_6.setText(self.show_name.text())
        elif self.count == 6:
            self.label_12.setText(self.show_name.text())
        elif self.count == 7:
            self.label_9.setText(self.show_name.text())
        elif self.count == 8:
            self.label_10.setText(self.show_name.text())
        elif self.count == 9:
            self.label_11.setText(self.show_name.text())
        elif self.count == 10:
            self.label_14.setText(self.show_name.text())
        elif self.count == 11:
            self.label_15.setText(self.show_name.text())
        elif self.count == 12:
            self.label_16.setText(self.show_name.text())
        elif self.count == 13:
            self.label_17.setText(self.show_name.text())
        elif self.count == 14:
            self.label_18.setText(self.show_name.text())
        elif self.count == 15:
            self.label_19.setText(self.show_name.text())
        elif self.count == 16:
            self.label_20.setText(self.show_name.text())
        elif self.count == 17:
            self.label_21.setText(self.show_name.text())
        elif self.count == 18:
            self.label_22.setText(self.show_name.text())
        else:
            print("结束了")

    def stop_click(self):
        if not self.flag:
            return
        self.flag = False

    def addText(self):
        text, ok = QInputDialog.getText(self, '添加', '输入姓名:')
        if ok:
            self.data.append(text)

        print("stop-------------------")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    luck = LuckyForm();
    luck.show()
    sys.exit(app.exec_())
