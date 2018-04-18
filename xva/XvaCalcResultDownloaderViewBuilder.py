from PyQt5 import QtWidgets

import requests
import json
import urllib

from PyQt5.QtWidgets import QHBoxLayout, QDialog, QVBoxLayout, QWidget, QPushButton, QAbstractItemView
from PyQt5.QtWidgets import QTableView

from XvaCalcRunTableModel import XvaCalcRunTableModel
from FileWriteHelper import FileWriteHelper

from constants import *


class XvaCalcResultDownloaderViewBuilder(QDialog):

    def __init__(self):
        super().__init__()
        self.token = None
        self.table_view = QTableView()
        self.model_builder = XvaCalcRunTableModel()
        self.file_writer = FileWriteHelper()
        self.table_view.setModel(self.model_builder.build_model([]))
        self.table_view.doubleClicked.connect(self.download_xva_results)
        self.table_view.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.download_btn = QPushButton("Download XVA Results")
        layout = QVBoxLayout(self)
        layout.addWidget(self.table_view)
        h_box = QHBoxLayout()
        buttons_panel = QWidget()
        buttons_panel.setLayout(h_box)
        h_box.addStretch(1)
        h_box.addWidget(self.download_btn)
        self.download_btn.clicked.connect(self.download_xva_results)
        h_box.addStretch(1)
        layout.addWidget(buttons_panel)

    def download_xva_calc_results(self, token):
        self.token = token
        criteria = r'{"filters": [{"op": "EQ", "name": "calculationType", "value": "XVA"}]}'
        response = requests.get(XVA_CALC_RUN, headers = {"Authorization":"Bearer " + token}, params= {"criteria" : criteria})
        data = json.loads(response.text)
        if data['statusCode'] == 0:
            self.table_view.setModel(self.model_builder.build_model(data['data']))
        else:
            QtWidgets.QErrorMessage().showMessage('Failed to Download XVA Calc results')

    def exec_(self, token):
        self.download_xva_calc_results(token)
        self.resize(1200, 800)
        super(XvaCalcResultDownloaderViewBuilder, self).exec_()

    def download_xva_results(self):
        indexes = self.table_view.selectionModel().selectedRows()
        if len(indexes) == 0:
            return
        for index in sorted(indexes):
            ref = self.table_view.model().item(index.row(), 1).text()
            # print('Row %d is selected which has calc run id : %s' % (index.row(), ref))
            response = requests.get(XVA_CALC_RESULT + "/" + ref, headers = {"Authorization":"Bearer " + self.token})
            # print(response.text)
            self.file_writer.write_blob(BULKSTORE_DOWNLOAD_DIR + "/" + "xva_" + ref, ref, response.text)

