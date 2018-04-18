import sys
import locale
import matplotlib.pyplot as plt
import traceback
import numpy as np

from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel

from ExposureModelBuilder import ExposureModelBuilder
from constants import *


class ExposureViewBuilder(QTabWidget):

    def __init__(self):
        super().__init__()
        # Model
        self.model = ExposureModelBuilder()
        # Tables
        self.matrix_table = QTableView()
        self.payment_matrix_table = QTableView()
        self.plot_exposures_btn = QPushButton("Plot")
        self.export_data_btn = QPushButton("Export CSV")
        self.payment_matrix_table.setStyleSheet("QHeaderView::section { background-color:silver }")
        # Tabs
        self.build_exposure_tab()
        # self.tabs.addTab(self.matrix_table, SUB_TAB_EXPOSURES_PLOT)
        self.addTab(self.payment_matrix_table, SUB_TAB_PAYMENT_MATRIX_PLOT)

    def build_exposure_tab(self):
        page = QWidget()
        v_box = QVBoxLayout()
        page.setLayout(v_box)
        # Table
        self.matrix_table.setStyleSheet("QHeaderView::section { background-color:silver }")
        v_box.addWidget(self.matrix_table, 1)
        h_box = QHBoxLayout()
        buttons_panel = QWidget()
        buttons_panel.setLayout(h_box)
        h_box.addStretch(1)
        h_box.addWidget(self.plot_exposures_btn)
        self.plot_exposures_btn.clicked.connect(self.plot_exposures)
        h_box.addWidget(self.export_data_btn)
        self.export_data_btn.clicked.connect(self.save_file_dialog)
        h_box.addStretch(1)
        v_box.addWidget(buttons_panel)
        self.addTab(page, SUB_TAB_EXPOSURES)

    def plot_exposures(self):
        self.plot_paths(self.model.matrix, self.model.dates)

    def build_model(self, fn):
        self.model.read_exposure_matrix(fn)
        self.add_table_items(self.matrix_table, self.model.matrix, self.model.dates)
        self.add_table_items(self.payment_matrix_table, self.model.payment_matrix, self.model.payment_dates)
        # self.plot_paths(self.model.matrix, self.model.dates);

    def export_data_to_csv(self, file_name):
        try:
            np.savetxt(file_name, self.model.matrix.transpose(), delimiter=",", header=",".join(self.model.dates))
        except:
            traceback.print_exc(file=sys.stdout)

    def save_file_dialog(self):
        if not self.matrix_table:
            QMessageBox.information(self, "Error", "Data is not loaded")
            return
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self,"Export CSV","","All Files (*);;CSV Files (*.csv)", options=options)
        if file_name:
            print(file_name)
            self.export_data_to_csv(file_name)

    def plot_paths(self, matrix, dates):
        try:
            if matrix is None:
                reply = QMessageBox.question(self, 'Message', "Load exposure matrix and try", QMessageBox.Ok)
            arr = matrix.transpose()

            n_lines = min(DEFAULT_NUM_OF_LINES, len(arr))
            for i in range(1, n_lines):
                plt.plot(arr[i])

            n_date_labels = max(DEFAULT_NUM_OF_DATES, len(dates))
            labels = list()
            idx = list()

            for i in range(0, len(dates), int(len(dates) * i / n_date_labels)):
                idx.append(i)
                labels.append(dates[i])

            plt.xticks(idx, labels, rotation='vertical')
            plt.show()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            traceback.print_exc()

    def add_table_items(self, table_view, matrix, dates):
        try:
            c = len(matrix)
            r = len(matrix[0])
            table_model = QStandardItemModel()
            table_model.setHorizontalHeaderLabels(dates)
            for i in range(0, c):
                for j in range(0, r):
                    table_model.setItem(j, i,  QStandardItem(locale.format('%.4f', matrix[i][j] if matrix[i][j] is not None else 0, True)))
            table_view.setModel(table_model)
        except:
            print("Unexpected error:", sys.exc_info()[0])
