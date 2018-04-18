import sys, traceback

from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel


class XvaCalcRunTableModel:

    def __init__(self):
        self.parsed_data = None
        self.table_model = QStandardItemModel()
        self.table_model.setHorizontalHeaderLabels(["Calc Run Id", "Request Ref", "Name", "Result Container", "Base Date", "State Code", "Last Updated"])

    def build_model(self, data):
        self.parsed_data = data
        i = 0
        for r in data:
            try:
                self.table_model.setItem(i, 0, QStandardItem(str(r['calculationRunId'])))
                self.table_model.setItem(i, 1, QStandardItem(r['requestRef']))
                self.table_model.setItem(i, 2, QStandardItem(r['dispName']))
                self.table_model.setItem(i, 3, QStandardItem(r['resultContainer']))
                self.table_model.setItem(i, 4, QStandardItem(r['baseDate']))
                self.table_model.setItem(i, 5, QStandardItem(r['stateCode']))
                self.table_model.setItem(i, 6, QStandardItem(r['lastUpdate']))
                i = i + 1
            except:
                traceback.print_exc(file=sys.stdout)
        return self.table_model


