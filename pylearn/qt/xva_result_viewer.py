from os import listdir
import locale
from os.path import isfile, isdir, join, basename
import json
from collections import OrderedDict
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Node:
    pass


class Measure:
    pass

locale.setlocale(locale.LC_NUMERIC, 'English')


def build_result_nodes(fn):
    nodes = list()
    if not fn or not isfile(fn):
        return nodes
    with open(fn, "r+") as f:
        data = json.load(f)
        results = data['results']
        # print("results length : ", len(results))
        for r in results:
            node = Node()
            node.resultType = r['resultType']
            node.calcType = r['calculationType']
            if 'tradeId' in r:
                node.tradeId = r['tradeId']
            if 'groupKey' in r:
                node.groupKey = r['groupKey']
            rk = r['resultKey']
            if not '-' in rk or not ':' in rk:
                continue
            node.params = rk.rsplit('-')[0].split(':')[1]
            node.measures = OrderedDict()
            for m in r['measures']:
                msr = Measure()
                msr.name = m['measureKey']
                msr.value = m['measureValue']
                msr.currency = m['currency'] if 'currency' in m else ''
                if 'currency' in m:
                    node.currency = m['currency']
                node.measures[msr.name] = msr
            nodes.append(node)
    return nodes


class XvaTreeModelBuilder:

    def __init__(self, resultNodes):
        self.model = QStandardItemModel()
        self.addTreeItems(self.model, resultNodes)

    def addTreeItems(self, parent, nodes):
        for n in nodes:
            if not hasattr(n, 'groupKey') :
                continue
            currencyNode = self.getCurrencyNode(n)
            rtNode = self.findOrAppend(currencyNode, n.resultType)
            hnodes = n.groupKey.split('|')
            parent = rtNode
            for hn in hnodes:
                if hn:
                    parent = self.findOrAppend(parent, hn)
            parent.setData(n)

    def getCurrencyNode(self, n):
        for r in range(self.model.rowCount(QModelIndex())):
            item = self.model.item(r, 0)
            if item.text() == n.currency:
                return item
        newItem = QStandardItem(n.currency)
        self.model.appendRow(newItem)
        return newItem

    def findOrAppend(self, parent, childName):
        for r in range(self.model.rowCount(self.model.indexFromItem(parent))):
            i = self.model.itemFromIndex(self.model.index(r, 0, parent.index()))
            if i.text() == childName:
                return i
        newItem = QStandardItem(childName)
        parent.appendRow(newItem)
        return newItem

    def getModel(self):
        return self.model


class XvaResultTree(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('XVA Result Viewer')

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.mainWidget = QWidget(self)
        self.treeView = QTreeView()
        self.tableView = QTableView()
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.buildModel("xva.json")
        #tree = XvaTreeModelBuilder(build_result_nodes("xva.json"))
        #self.model = tree.getModel()
        #self.treeView.setModel(self.model)

        layout = QHBoxLayout(self.mainWidget)

        left = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        left.setHorizontalStretch(1)
        self.treeView.setSizePolicy(left)
        layout.addWidget(self.treeView)

        right = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        right.setHorizontalStretch(3)
        self.tableView.setSizePolicy(right)
        layout.addWidget(self.tableView)
        self.setCentralWidget(self.mainWidget)
        self.showMaximized()

    def buildModel(self, fn):
        tree = XvaTreeModelBuilder(build_result_nodes(fn))
        self.model = tree.getModel()
        self.treeView.setModel(self.model)
        treeSelectionModel = self.treeView.selectionModel()
        treeSelectionModel.selectionChanged.connect(self.addTableItems)

    def addTableItems(self, selected, deselected):
        # Find the top-level item in the tree.
        treeIndex = selected.indexes()[0]
        print(treeIndex)
        if self.model.hasChildren(treeIndex):
            return

        item = self.model.itemFromIndex(treeIndex)
        print(item.text)
        dat = item.data().measures
        self.tableModel = QStandardItemModel()

        c=0
        for k, v in dat.items():
            if isinstance(v.value, float):
                self.tableModel.setItem(0, c, QStandardItem(k))
                self.tableModel.setItem(1, c, QStandardItem(locale.format('%.2f', v.value, True)))
                c += 1

        self.tableView.setModel(self.tableModel)

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        print("Selected file : ", fname[0])
        self.buildModel(fname[0])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = XvaResultTree()
    window.show()
    sys.exit(app.exec_())

