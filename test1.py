import sys


from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit, QComboBox, QApplication


class Combo(QComboBox):
    def __init__(self, title, parent):
        super(Combo, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print("---------------")
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e):
        print(e)


    def dropEvent(self, e):
        self.addItem(e.mimeData().text())
        for i in range(self.count()):
            print(self.itemText(i))


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        lo = QFormLayout()
        label = QLabel("拖拽测试")
        lo.addRow(label)

        edit = QLineEdit()
        edit.setDragEnabled(True)
        com = Combo("button", self)
        lo.addRow(edit,com)
        self.setLayout(lo)
        self.setWindowTitle("拖拽的例子")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())