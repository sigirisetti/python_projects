import locale
import sys, traceback
import requests
import os, errno
import json

from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QProgressDialog

from XvaResultTreeModelBuilder import XvaTreeModelBuilder
from XvaResultJsonParser import build_result_nodes
from XvaResultJsonParser import Measure

from constants import *


class XvaResultTreeViewBuilder(QWidget):

    def __init__(self):
        super().__init__()
        # Models
        self.model = None
        self.table_model = None
        self.file_name = None
        self.tree_model = None
        # Widget layout
        layout = QHBoxLayout(self)
        # XVA result views
        self.tree_view = QTreeView()
        self.table_view = QTableView()
        self.table_view.setStyleSheet("QHeaderView::section { background-color:silver }")
        self.table_view.horizontalHeader().setStretchLastSection(True)
        self.build_model('')
        # Left side of Widget
        left = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        left.setHorizontalStretch(1)
        self.tree_view.setSizePolicy(left)
        layout.addWidget(self.tree_view)
        # Right side of Widget
        right = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        right.setHorizontalStretch(3)
        self.table_view.setSizePolicy(right)
        layout.addWidget(self.table_view)

    def build_model(self, fn):
        try:
            self.file_name = fn
            self.tree_model = XvaTreeModelBuilder(build_result_nodes(fn))
        except:
            print("Unexpected error: ", sys.exc_info()[0])
            print("Unexpected error: ", sys.exc_info()[1])
            traceback.print_exc(file=sys.stdout)

        self.model = self.tree_model.get_model()
        self.tree_view.setModel(self.model)
        tree_selection_model = self.tree_view.selectionModel()
        tree_selection_model.selectionChanged.connect(self.add_table_items)

    def add_table_items(self, selected, deselected):
        tree_index = selected.indexes()[0]
        #print("Tree index - ", tree_index)
        # if self.model.hasChildren(tree_index):
        #    return
        item = self.model.itemFromIndex(tree_index)
        if not item.data():
            print("No data in item - ", item.text())
            return
        dat = item.data().measures
        self.table_model = QStandardItemModel()
        headers = list();
        c = 0
        for k, v in dat.items():
            if k == 'UTCDATE':
                continue
            if isinstance(v.value, float) or isinstance(v.value, int):
                headers.append(k)
                self.table_model.setItem(0, c, QStandardItem(
                    locale.format('%d' if isinstance(v.value, int) else '%.2f', v.value if v.value is not None else 0,
                                  True)))
                c += 1
            elif isinstance(v.value, list):
                headers.append(k)
                for idx, val in enumerate(v.value):
                    cell_value = ''
                    if isinstance(val, float):
                        cell_value = locale.format('%.2f', v.value[idx] if v.value[idx] is not None else 0, True)
                    else:
                        print(type(v.value[idx]))
                        cell_value = str(v.value[idx])
                    self.table_model.setItem(idx, c, QStandardItem(cell_value))
                c += 1
            elif type(v) is Measure:
                headers.append(k)
                self.table_model.setItem(0, c, QStandardItem(v.value))
                c += 1
            else:
                print("Skipping display measure - ", k, type(v.value))
        self.table_model.setHorizontalHeaderLabels(headers)

        self.table_view.setModel(self.table_model)

    def download_bulk_stores(self):
        locators = self.tree_model.download_bulk_stores(self.file_name)
        if not locators:
            QMessageBox.information(self, "Message", "You did not select any xva results")
            return

        progress = QProgressDialog("Downloading files...", "Abort", 0, len(locators), self);
        progress.setModal(True)

        n = 0
        for locator in locators:
            if progress.wasCanceled():
                break
            print("Downloading -- ", locator)
            obj = json.loads(locator[(locator.index(":") + 1):])
            output_name = obj['outputName_m']
            if output_name == "EXPOSURE":
                output_name = output_name + "_" + obj['identifier_m']
            response = requests.get(EXPOSURE_DOWNLOAD_URL, params={"bulkStoreLocator": locator})
            contents = response.text
            self.write_blob(output_name, contents)
            n = n+1
            progress.setValue(n)
        progress.setValue(len(locators))

    def write_blob(self, output_name, contents):
        h, t = os.path.split(self.file_name)
        dir = BULKSTORE_DOWNLOAD_DIR + t[0:t.index(".")]
        if not os.path.exists(dir):
            try:
                os.makedirs(dir)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        fh = open(dir + "/" + output_name + ".json", "w")
        fh.write(contents)
        fh.close()
