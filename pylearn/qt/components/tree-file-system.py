import sys
from os import listdir
from os.path import isfile, isdir, join, basename
import json
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon


def inspect():
    tradeResultKeys =list()
    groupResultKeys =list()
    topNodes = dict()
    with open("xva_terms_portfolio.json", "r+") as f:
        data = json.load(f)
        results = data['results']
        print("results length : ", len(results))
        for r in results:
            # print("====================================================================")
            # print(r['resultKey'])
            if 'groupKey' in r :
                groupResultKeys.append(r['resultKey'])
            else:
                tradeResultKeys.append(r['resultKey'])

            # measures = r['measures']
            # print({m['measureKey']:type(m['measureValue']) for m in measures})
    # print("====================================================================")
    # print("result types : ", resultType)
    print("==============================   GROUP KEYS ======================================")
    for key in sorted(groupResultKeys):
        print(key)
    print("==============================   TRADE KEYS ======================================")
    for key in sorted(tradeResultKeys):
        print(key)



class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file system view - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.tree = QTreeView()
        self.tree.setModel(self.model)

        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)

        self.tree.setWindowTitle("Dir View")
        self.tree.resize(640, 480)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.tree)
        self.setLayout(windowLayout)

        self.show()


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ex = App()
    # sys.exit(app.exec_())
    inspect()