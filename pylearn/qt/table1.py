from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        self.table = QTableWidget(parent=self)
        self.table.setColumnCount(2)
        self.table.setRowCount(2)
        self.table.setHorizontalHeaderLabels(['col1','col2'])
        self.table.setVerticalHeaderLabels(['row1','row2'])
        self.table.setItem(0,0,QTableWidgetItem('foo'))
        self.table.setItem(0,1,QTableWidgetItem('bar'))
        self.table.setItem(1,0,QTableWidgetItem('baz'))
        self.table.setItem(1,1,QTableWidgetItem('qux'))

        layout = QGridLayout()
        layout.addWidget(self.table, 1, 0)
        self.setLayout(layout)

        self.clip = QApplication.clipboard()
        self.show()


    def keyPressEvent(self, e):
        if (e.modifiers() & QtCore.Qt.ControlModifier):
            selected = self.table.selectedRanges()

            if e.key() == QtCore.Qt.Key_C: #copy
                s = '\t'+"\t".join([str(self.table.horizontalHeaderItem(i).text()) for i in range(selected[0].leftColumn(), selected[0].rightColumn()+1)])
                s = s + '\n'

                for r in range(selected[0].topRow(), selected[0].bottomRow()+1):
                    s += self.table.verticalHeaderItem(r).text() + '\t'
                    for c in range(selected[0].leftColumn(), selected[0].rightColumn()+1):
                        try:
                            s += str(self.table.item(r,c).text()) + "\t"
                        except AttributeError:
                            s += "\t"
                    s = s[:-1] + "\n" #eliminate last '\t'
                self.clip.setText(s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())
