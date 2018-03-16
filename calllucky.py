import sys
import threading
import time
from PyQt5.QtWidgets import QWidget, QApplication

from lucky import Ui_Form


class LuckyForm(QWidget,Ui_Form):
    def __init__(self, parent=None):
        super(LuckyForm, self).__init__(parent)
        self.initData()
        self.setupUi(self)
        self.initView()

    def initData(self):
        self.data = ["A", "B", "C", "D", "E", "F", "G", "H"]

    def initView(self):
        self.roll.clicked.connect(self.roll_click)
        self.stop.clicked.connect(self.stop_click)

    def roll_click(self):
        print("roll----------------")
        t = threading.Thread(target=self.start_roll, name='start_roll')
        t.start()
        t.join()


    def start_roll(self):
        while True:
            for item in self.data:
                time.sleep(1)
                self.show_name.setText(item)


    def stop_click(self):
        print("stop-------------------")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    luck = LuckyForm();
    luck.show()
    sys.exit(app.exec_())
